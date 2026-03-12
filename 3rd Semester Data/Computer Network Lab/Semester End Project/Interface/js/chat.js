// Check login
if (!localStorage.getItem('userName')) {
  window.location.href = 'login.html';
}

const userName = localStorage.getItem('userName');
const userDept = localStorage.getItem('userDept');
const userAvatar = localStorage.getItem('userAvatar');

document.getElementById('userName').textContent = userName;
document.getElementById('userAvatar').textContent = userAvatar;

// Socket.io connection
const socket = io('http://localhost:3000');

let currentRoom = 'general';

// Elements
const messagesDiv = document.getElementById('messages');
const messageInput = document.getElementById('messageInput');
const sendBtn = document.getElementById('sendBtn');
const channelList = document.getElementById('channelList');
const currentChannel = document.getElementById('currentChannel');
const typingIndicator = document.getElementById('typingIndicator');

// Join server
socket.emit('join', { name: userName, department: userDept });

// Switch channel
channelList.addEventListener('click', (e) => {
  if (e.target.classList.contains('channel')) {
    document.querySelector('.channel.active').classList.remove('active');
    e.target.classList.add('active');
    currentRoom = e.target.dataset.room;
    currentChannel.textContent = `# ${currentRoom.charAt(0).toUpperCase() + currentRoom.slice(1)}`;
    socket.emit('switchRoom', currentRoom);
    messagesDiv.innerHTML = '';
  }
});

// Load old messages
socket.on('loadMessages', (msgs) => {
  messagesDiv.innerHTML = '';
  msgs.forEach(msg => displayMessage(msg));
  scrollToBottom();
});

// New message
socket.on('newMessage', (msg) => {
  displayMessage(msg);
  scrollToBottom();
});

// Typing indicator
let typingTimer;
messageInput.addEventListener('input', () => {
  socket.emit('typing', { room: currentRoom, isTyping: true });
  clearTimeout(typingTimer);
  typingTimer = setTimeout(() => {
    socket.emit('typing', { room: currentRoom, isTyping: false });
  }, 1000);
});

socket.on('userTyping', ({ name, isTyping }) => {
  if (isTyping) {
    typingIndicator.textContent = `${name} is typing...`;
  } else {
    typingIndicator.textContent = '';
  }
});

// Display message
function displayMessage(msg) {
  const div = document.createElement('div');
  div.classList.add('message');
  if (msg.name === userName) div.classList.add('own');

  div.innerHTML = `
    <div class="sender">${msg.name}</div>
    <div>${msg.text}</div>
    <div class="time">${new Date(msg.timestamp).toLocaleTimeString()}</div>
  `;
  messagesDiv.appendChild(div);
}

// Send message
function sendMessage() {
  const text = messageInput.value.trim();
  if (text) {
    socket.emit('sendMessage', { room: currentRoom, text });
    messageInput.value = '';
  }
}

sendBtn.addEventListener('click', sendMessage);
messageInput.addEventListener('keypress', (e) => {
  if (e.key === 'Enter') sendMessage();
});

function scrollToBottom() {
  messagesDiv.scrollTop = messagesDiv.scrollHeight;
}

// Logout
document.getElementById('logoutBtn').addEventListener('click', () => {
  localStorage.clear();
  window.location.href = 'login.html';
});

