const express = require('express');
const http = require('http');
const socketIo = require('socket.io');
const path = require('path');

const app = express();
const server = http.createServer(app);
const io = socketIo(server, {
  cors: {
    origin: "*",
    methods: ["GET", "POST"]
  }
});

// Serve static files (HTML, CSS, JS) from the parent directory
app.use(express.static(path.join(__dirname, '..')));

// Store online users: socket.id -> { name, department }
const users = new Map();

// Store messages per room (in-memory for demo)
const messages = {
  general: [],
  hr: [],
  finance: [],
  development: [],
  testing: [],
  management: []
};

io.on('connection', (socket) => {
  console.log('A user connected:', socket.id);

  // User joins with name and department
  socket.on('join', ({ name, department }) => {
    users.set(socket.id, { name, department });
    socket.join('general'); // Default room

    // Send chat history for general channel
    socket.emit('loadMessages', messages['general']);

    // Notify all clients about new online user
    io.emit('onlineUsers', Array.from(users.values()).map(u => u.name));
  });

  // Switch to a different room/channel
  socket.on('switchRoom', (room) => {
    // Leave all previous rooms
    Object.keys(messages).forEach(r => socket.leave(r));
    
    socket.join(room);
    socket.emit('loadMessages', messages[room] || []);
  });

  // Receive and broadcast new message
  socket.on('sendMessage', ({ room, text }) => {
    const user = users.get(socket.id);
    if (!user) return;

    const message = {
      name: user.name,
      text: text.trim(),
      timestamp: new Date().toISOString(),
      room
    };

    // Save message
    if (!messages[room]) messages[room] = [];
    messages[room].push(message);

    // Keep only last 100 messages per room
    if (messages[room].length > 100) {
      messages[room].shift();
    }

    // Broadcast to everyone in the room
    io.to(room).emit('newMessage', message);
  });

  // Typing indicator
  socket.on('typing', ({ room, isTyping }) => {
    const user = users.get(socket.id);
    if (user) {
      socket.to(room).emit('userTyping', {
        name: user.name,
        isTyping
      });
    }
  });

  // Handle user disconnect
  socket.on('disconnect', () => {
    const user = users.get(socket.id);
    if (user) {
      users.delete(socket.id);

      // Update online users list for all clients
      io.emit('onlineUsers', Array.from(users.values()).map(u => u.name));
      
      console.log('User disconnected:', user.name, socket.id);
    } else {
      console.log('User disconnected:', socket.id);
    }
  });
});

const PORT = process.env.PORT || 3000;
server.listen(PORT, () => {
  console.log(`Server running on http://localhost:${PORT}`);
  console.log(`Open login.html in your browser to start chatting!`);
});