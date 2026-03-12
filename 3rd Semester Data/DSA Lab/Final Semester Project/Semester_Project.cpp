#include<iostream>
#include<fstream>
#include<string>
#include<vector>
#include<algorithm>
#include<cstdlib>
#include<ctime>
#include<iomanip>
#include<sstream>
#include<map>
#include<cctype>
#include<utility>
using namespace std;

struct Anime{
    int id;
    string name;
    string genre;
    int year;
    double rating;
    int episodes;
    string studio;
    
    void display()const{
        cout<<left<<setw(6)<<id
            <<setw(40)<<(name.length()>38?name.substr(0,35)+"...":name)
            <<setw(25)<<(genre.length()>23?genre.substr(0,20)+"...":genre)
            <<setw(8)<<year
            <<setw(8)<<fixed<<setprecision(1)<<rating
            <<setw(10)<<episodes
            <<setw(20)<<(studio.length()>18?studio.substr(0,15)+"...":studio)<<endl;
    }
    
    void displayFull()const{
        cout<<"\n========================"<<endl;
        cout<<"      ANIME DETAILS     "<<endl;
        cout<<"========================"<<endl;
        cout<<"ID:        "<<id<<endl;
        cout<<"Name:      "<<name<<endl;
        cout<<"Genre:     "<<genre<<endl;
        cout<<"Year:      "<<year<<endl;
        cout<<"Rating:    "<<fixed<<setprecision(1)<<rating<<"/10.0"<<endl;
        cout<<"Episodes:  "<<episodes<<endl;
        cout<<"Studio:    "<<studio<<endl;
        cout<<"========================\n"<<endl;
    }
};

int stringToInt(const string&str){
    int result=0;
    bool isNegative=false;
    int i=0;
    int len=str.length();
    if(len==0)return 0;
    while(i<len&&(str[i]==' '||str[i]=='\t'))i++;
    if(i<len&&str[i]=='-'){
        isNegative=true;
        i++;
    }
    while(i<len){
        char c=str[i];
        if(c>='0'&&c<='9'){
            result=result*10+(c-'0');
        }else{
            break;
        }
        i++;
    }
    return isNegative?-result:result;
}

double stringToDouble(const string&str){
    double result=0.0;
    bool isNegative=false;
    bool decimalFound=false;
    double decimalPlace=0.1;
    int i=0;
    int len=str.length();
    if(len==0)return 0.0;
    while(i<len&&(str[i]==' '||str[i]=='\t'))i++;
    if(i<len&&str[i]=='-'){
        isNegative=true;
        i++;
    }
    while(i<len){
        char c=str[i];
        if(c>='0'&&c<='9'){
            if(!decimalFound){
                result=result*10.0+(c-'0');
            }else{
                result+=(c-'0')*decimalPlace;
                decimalPlace/=10.0;
            }
        }else if(c=='.'&&!decimalFound){
            decimalFound=true;
        }else{
            break;
        }
        i++;
    }
    return isNegative?-result:result;
}

class AnimeDatabase{
private:
    vector<Anime>animeList;
    
    string toLower(const string&str){
        string result=str;
        for(int i=0;i<result.length();i++){
            result[i]=tolower(result[i]);
        }
        return result;
    }
    
public:
    bool loadFromFile(const string&filename){
        ifstream file(filename.c_str());
        if(!file.is_open()){
            cout<<"Error: Cannot open file: "<<filename<<endl;
            return false;
        }
        animeList.clear();
        string line;
        int fieldNum=0;
        Anime current;
        int count=0;
        cout<<"Loading Anime Data..."<<endl;
        while(getline(file,line)){
            if(!line.empty()&&line[line.length()-1]=='\r'){
                line=line.substr(0,line.length()-1);
            }
            if(line.empty())continue;
            switch(fieldNum){
                case 0:
                    current.id=stringToInt(line);
                    if(current.id<=0)current.id=animeList.size()+1;
                    break;
                case 1:
                    current.name=line;
                    break;
                case 2:
                    current.genre=line;
                    break;
                case 3:
                    current.year=stringToInt(line);
                    if(current.year<1900||current.year>2024)current.year=2000;
                    break;
                case 4:
                    current.rating=stringToDouble(line);
                    if(current.rating<0.0)current.rating=0.0;
                    if(current.rating>10.0)current.rating=10.0;
                    break;
                case 5:
                    current.episodes=stringToInt(line);
                    if(current.episodes<0)current.episodes=0;
                    break;
                case 6:
                    current.studio=line;
                    animeList.push_back(current);
                    count++;
                    break;
            }
            fieldNum=(fieldNum+1)%7;
        }
        file.close();
        if(animeList.empty()){
            cout<<"No data loaded."<<endl;
            return false;
        }
        cout<<"Successfully loaded "<<animeList.size()<<" anime records!\n"<<endl;
        return true;
    }
    
    bool saveToFile(const string&filename){
        ofstream file(filename.c_str());
        if(!file.is_open()){
            cout<<"Error: Cannot write to file: "<<filename<<endl;
            return false;
        }
        for(int i=0;i<animeList.size();i++){
            const Anime&a=animeList[i];
            file<<a.id<<endl;
            file<<a.name<<endl;
            file<<a.genre<<endl;
            file<<a.year<<endl;
            file<<fixed<<setprecision(1)<<a.rating<<endl;
            file<<a.episodes<<endl;
            file<<a.studio<<endl;
        }
        file.close();
        cout<<"Saved "<<animeList.size()<<" anime to "<<filename<<endl;
        return true;
    }
    
    Anime*getAnimeById(int id){
        for(int i=0;i<animeList.size();i++){
            if(animeList[i].id==id){
                return &animeList[i];
            }
        }
        return NULL;
    }
    
    void addAnime(const Anime&anime){
        for(int i=0;i<animeList.size();i++){
            if(animeList[i].id==anime.id){
                cout<<"Error: ID "<<anime.id<<" already exists!"<<endl;
                return;
            }
        }
        animeList.push_back(anime);
        cout<<"Added anime: "<<anime.name<<" (ID: "<<anime.id<<")\n"<<endl;
    }
    
    bool deleteAnime(int id){
        for(int i=0;i<animeList.size();i++){
            if(animeList[i].id==id){
                string name=animeList[i].name;
                animeList.erase(animeList.begin()+i);
                cout<<"Deleted anime: "<<name<<" (ID: "<<id<<")\n"<<endl;
                return true;
            }
        }
        cout<<"Error: ID "<<id<<" not found!\n"<<endl;
        return false;
    }
    
    int getCount()const{return animeList.size();}
    bool isEmpty()const{return animeList.empty();}
    
    void clear(){
        animeList.clear();
        cout<<"Database cleared.\n"<<endl;
    }
    
    void displayAll(){
        if(animeList.empty()){
            cout<<"Database is empty!"<<endl;
            return;
        }
        const int PAGE_SIZE=50;
        int currentPage=0;
        string input;
        do{
            int start=currentPage*PAGE_SIZE;
            int end=start+PAGE_SIZE;
            cout<<"\n"<<string(115,'=')<<endl;
            cout<<left<<setw(6)<<"ID"
                <<setw(40)<<"Name"
                <<setw(25)<<"Genre"
                <<setw(8)<<"Year"
                <<setw(8)<<"Rating"
                <<setw(10)<<"Episodes"
                <<setw(20)<<"Studio"<<endl;
            cout<<string(115,'-')<<endl;
            for(int i=start;i<end&&i<animeList.size();i++){
                animeList[i].display();
            }
            cout<<string(115,'=')<<endl;
            cout<<"Showing "<<start+1<<"-"<<min(end,(int)animeList.size())
                <<" of "<<animeList.size()<<" anime"<<endl;
            if(end<animeList.size()){
                cout<<"\nOptions:"<<endl;
                cout<<"  n - Next page"<<endl;
                cout<<"  p - Previous page"<<endl;
                cout<<"  s - Stop viewing"<<endl;
                cout<<"\nEnter choice: ";
                getline(cin,input);
                if(input=="s"||input=="S"){
                    break;
                }else if(input=="n"||input=="N"||input.empty()){
                    currentPage++;
                }else if(input=="p"||input=="P"){
                    if(currentPage>0)currentPage--;
                }else{
                    currentPage++;
                }
            }else{
                cout<<"\nEnd of list reached."<<endl;
                break;
            }
        }while(true);
        cout<<endl;
    }
    
    vector<Anime*>searchByName(const string&name){
        vector<Anime*>results;
        string searchName=toLower(name);
        for(int i=0;i<animeList.size();i++){
            string animeName=toLower(animeList[i].name);
            if(animeName.find(searchName)!=string::npos){
                results.push_back(&animeList[i]);
            }
        }
        return results;
    }
    
    vector<Anime*>searchByGenre(const string&genre){
        vector<Anime*>results;
        string searchGenre=toLower(genre);
        for(int i=0;i<animeList.size();i++){
            string animeGenre=toLower(animeList[i].genre);
            if(animeGenre.find(searchGenre)!=string::npos){
                results.push_back(&animeList[i]);
            }
        }
        return results;
    }
    
    vector<Anime*>searchByStudio(const string&studio){
        vector<Anime*>results;
        string searchStudio=toLower(studio);
        for(int i=0;i<animeList.size();i++){
            string animeStudio=toLower(animeList[i].studio);
            if(animeStudio.find(searchStudio)!=string::npos){
                results.push_back(&animeList[i]);
            }
        }
        return results;
    }
    
    void displayTopAnime(int category, int limit = 10) {
        if (animeList.empty()) {
            cout << "Database is empty!" << endl;
            return;
        }
        
        vector<Anime> sortedList = animeList;
        
        switch(category) {
            case 1: // By Rating (Highest First)
                sort(sortedList.begin(), sortedList.end(), 
                    [](const Anime& a, const Anime& b) { return a.rating > b.rating; });
                cout << "\n" << string(115,'=') << endl;
                cout << "                    TOP " << limit << " ANIME BY RATING                    " << endl;
                cout << string(115,'=') << endl;
                break;
                
            case 2: // By Year (Newest First)
                sort(sortedList.begin(), sortedList.end(), 
                    [](const Anime& a, const Anime& b) { return a.year > b.year; });
                cout << "\n" << string(115,'=') << endl;
                cout << "                TOP " << limit << " NEWEST ANIME                    " << endl;
                cout << string(115,'=') << endl;
                break;
                
            case 3: // By Episodes (Most First)
                sort(sortedList.begin(), sortedList.end(), 
                    [](const Anime& a, const Anime& b) { return a.episodes > b.episodes; });
                cout << "\n" << string(115,'=') << endl;
                cout << "           TOP " << limit << " ANIME BY EPISODE COUNT               " << endl;
                cout << string(115,'=') << endl;
                break;
                
            case 4: // Oldest Anime
                sort(sortedList.begin(), sortedList.end(), 
                    [](const Anime& a, const Anime& b) { return a.year < b.year; });
                cout << "\n" << string(115,'=') << endl;
                cout << "               TOP " << limit << " OLDEST ANIME                    " << endl;
                cout << string(115,'=') << endl;
                break;
        }
        
        cout << left << setw(6) << "Rank"
             << setw(6) << "ID"
             << setw(40) << "Name"
             << setw(25) << "Genre"
             << setw(8) << "Year"
             << setw(8) << "Rating"
             << setw(10) << "Episodes"
             << setw(20) << "Studio" << endl;
        cout << string(115,'-') << endl;
        
        for (int i = 0; i < min(limit, (int)sortedList.size()); i++) {
            cout << left << setw(6) << i+1;
            sortedList[i].display();
        }
        
        cout << string(115,'=') << endl << endl;
    }
    
    void displayStatistics() {
        if (animeList.empty()) {
            cout << "Database is empty!" << endl;
            return;
        }
        
        cout << "\n" << string(50,'=') << endl;
        cout << "         ANIME DATABASE STATISTICS          " << endl;
        cout << string(50,'=') << endl;
        
        // Calculate average rating
        double totalRating = 0;
        double maxRating = 0;
        double minRating = 10;
        int newestYear = 0;
        int oldestYear = 2024;
        int totalEpisodes = 0;
        map<string, int> genreCount;
        map<string, int> studioCount;
        
        for (const auto& anime : animeList) {
            totalRating += anime.rating;
            if (anime.rating > maxRating) maxRating = anime.rating;
            if (anime.rating < minRating) minRating = anime.rating;
            if (anime.year > newestYear) newestYear = anime.year;
            if (anime.year < oldestYear) oldestYear = anime.year;
            totalEpisodes += anime.episodes;
            
            // Count genres
            stringstream ss(anime.genre);
            string genre;
            while (getline(ss, genre, ',')) {
                genre.erase(0, genre.find_first_not_of(" "));
                genre.erase(genre.find_last_not_of(" ") + 1);
                genreCount[genre]++;
            }
            
            // Count studios
            studioCount[anime.studio]++;
        }
        
        double avgRating = totalRating / animeList.size();
        
        cout << "Total Anime:       " << animeList.size() << endl;
        cout << "Average Rating:    " << fixed << setprecision(2) << avgRating << "/10.0" << endl;
        cout << "Highest Rating:    " << fixed << setprecision(1) << maxRating << "/10.0" << endl;
        cout << "Lowest Rating:     " << fixed << setprecision(1) << minRating << "/10.0" << endl;
        cout << "Newest Anime:      " << newestYear << endl;
        cout << "Oldest Anime:      " << oldestYear << endl;
        cout << "Total Episodes:    " << totalEpisodes << endl;
        cout << "Average Episodes:  " << fixed << setprecision(0) << (double)totalEpisodes / animeList.size() << endl;
        
        // Find top genres
        vector<pair<string, int>> genreVec(genreCount.begin(), genreCount.end());
        sort(genreVec.begin(), genreVec.end(), 
            [](const pair<string, int>& a, const pair<string, int>& b) { return a.second > b.second; });
        
        cout << "\nTop 5 Genres:" << endl;
        for (int i = 0; i < min(5, (int)genreVec.size()); i++) {
            cout << "  " << i+1 << ". " << left << setw(20) << genreVec[i].first 
                 << " (" << genreVec[i].second << " anime)" << endl;
        }
        
        // Find top studios
        vector<pair<string, int>> studioVec(studioCount.begin(), studioCount.end());
        sort(studioVec.begin(), studioVec.end(), 
            [](const pair<string, int>& a, const pair<string, int>& b) { return a.second > b.second; });
        
        cout << "\nTop 5 Studios:" << endl;
        for (int i = 0; i < min(5, (int)studioVec.size()); i++) {
            cout << "  " << i+1 << ". " << left << setw(20) << studioVec[i].first 
                 << " (" << studioVec[i].second << " anime)" << endl;
        }
        
        cout << string(50,'=') << endl << endl;
    }
};

Anime getAnimeFromUser(){
    Anime anime;
    string input;
    cout<<"\n========================"<<endl;
    cout<<"     ADD NEW ANIME     "<<endl;
    cout<<"========================"<<endl;
    while(true){
        cout<<"ID: ";
        getline(cin,input);
        anime.id=stringToInt(input);
        if(anime.id>0){
            break;
        }
        cout<<"Invalid ID! Must be positive number."<<endl;
    }
    cout<<"Name: ";
    getline(cin,anime.name);
    cout<<"Genre: ";
    getline(cin,anime.genre);
    while(true){
        cout<<"Year (1900-2024): ";
        getline(cin,input);
        anime.year=stringToInt(input);
        if(anime.year>=1900&&anime.year<=2024){
            break;
        }
        cout<<"Invalid year! Must be 1900-2024."<<endl;
    }
    while(true){
        cout<<"Rating (0.0-10.0): ";
        getline(cin,input);
        anime.rating=stringToDouble(input);
        if(anime.rating>=0.0&&anime.rating<=10.0){
            break;
        }
        cout<<"Invalid rating! Must be 0.0-10.0."<<endl;
    }
    while(true){
        cout<<"Episodes: ";
        getline(cin,input);
        anime.episodes=stringToInt(input);
        if(anime.episodes>=0){
            break;
        }
        cout<<"Invalid episode count! Must be non-negative."<<endl;
    }
    cout<<"Studio: ";
    getline(cin,anime.studio);
    return anime;
}

void topAnimeMenu(AnimeDatabase& db) {
    int choice = -1;
    string input;
    do {
        cout << "\n========================" << endl;
        cout << "      TOP ANIME MENU     " << endl;
        cout << "========================" << endl;
        cout << "1. Top by Rating" << endl;
        cout << "2. Top by Year (Newest)" << endl;
        cout << "3. Top by Episode Count" << endl;
        cout << "4. Top Oldest Anime" << endl;
        cout << "5. Custom Top N" << endl;
        cout << "0. Back to main menu" << endl;
        cout << "========================" << endl;
        cout << "Enter choice: ";
        getline(cin, input);
        choice = stringToInt(input);
        
        switch(choice) {
            case 1:
            case 2:
            case 3:
            case 4:
                db.displayTopAnime(choice);
                break;
            case 5: {
                cout << "Select category:" << endl;
                cout << "1. By Rating" << endl;
                cout << "2. By Year (Newest)" << endl;
                cout << "3. By Episode Count" << endl;
                cout << "4. Oldest Anime" << endl;
                cout << "Enter category choice: ";
                getline(cin, input);
                int category = stringToInt(input);
                
                if (category < 1 || category > 4) {
                    cout << "Invalid category!" << endl;
                    break;
                }
                
                cout << "How many anime to display? (1-50): ";
                getline(cin, input);
                int limit = stringToInt(input);
                
                if (limit < 1) limit = 10;
                if (limit > 50) limit = 50;
                
                db.displayTopAnime(category, limit);
                break;
            }
            case 0:
                cout << "Returning to main menu..." << endl;
                break;
            default:
                cout << "Invalid choice!" << endl;
        }
        
        if (choice != 0) {
            cout << "\nPress Enter to continue...";
            getline(cin, input);
        }
    } while (choice != 0);
}

void showMainMenu(){
    cout<<"\n========================================="<<endl;
    cout<<"   ANIME DATABASE MANAGEMENT SYSTEM     "<<endl;
    cout<<"========================================="<<endl;
    cout<<"1. Display all anime (paged)"<<endl;
    cout<<"2. Search by ID"<<endl;
    cout<<"3. Search by name"<<endl;
    cout<<"4. Search by genre"<<endl;
    cout<<"5. Search by studio"<<endl;
    cout<<"6. Add new anime"<<endl;
    cout<<"7. Delete anime"<<endl;
    cout<<"8. Top Anime Lists"<<endl;
    cout<<"9. View Statistics"<<endl;
    cout<<"10. Load from file"<<endl;
    cout<<"11. Save to file"<<endl;
    cout<<"12. Clear database"<<endl;
    cout<<"13. Show count"<<endl;
    cout<<"0. Exit"<<endl;
    cout<<"========================================="<<endl;
    cout<<"Enter choice: ";
}

int main(){
    AnimeDatabase db;
    cout<<"\n========================================="<<endl;
    cout<<"      ANIME DATABASE SYSTEM v2.0        "<<endl;
    cout<<"=========================================\n"<<endl;
    cout<<"Loading data from anime_data.txt..."<<endl;
    if(!db.loadFromFile("anime_data.txt")){
        cout<<"\nCreating sample data..."<<endl;
        ofstream file("sample_anime.txt");
        if(file){
            file<<"1\nAttack on Titan\nAction, Drama, Fantasy\n2013\n9.1\n75\nWit Studio\n";
            file<<"2\nFullmetal Alchemist: Brotherhood\nAction, Adventure, Drama\n2009\n9.2\n64\nBones\n";
            file<<"3\nDeath Note\nMystery, Psychological, Thriller\n2006\n8.8\n37\nMadhouse\n";
            file<<"4\nOne Punch Man\nAction, Comedy, Sci-Fi\n2015\n8.7\n24\nMadhouse\n";
            file<<"5\nDemon Slayer\nAction, Fantasy\n2019\n8.9\n55\nufotable\n";
            file<<"6\nMy Hero Academia\nAction, Comedy, School\n2016\n8.4\n113\nBones\n";
            file<<"7\nHunter x Hunter\nAction, Adventure, Fantasy\n2011\n9.1\n148\nMadhouse\n";
            file<<"8\nNaruto Shippuden\nAction, Adventure, Fantasy\n2007\n8.7\n500\nPierrot\n";
            file<<"9\nOne Piece\nAction, Adventure, Fantasy\n1999\n9.0\n1100+\nToei Animation\n";
            file<<"10\nSteins;Gate\nSci-Fi, Thriller\n2011\n9.1\n24\nWhite Fox\n";
            file.close();
            cout<<"Created sample file: sample_anime.txt"<<endl;
        }
        db.loadFromFile("sample_anime.txt");
    }
    int choice=-1;
    string input;
    do{
        showMainMenu();
        getline(cin,input);
        choice=stringToInt(input);
        switch(choice){
            case 1:
                db.displayAll();
                break;
            case 2:{
                cout<<"Enter anime ID: ";
                getline(cin,input);
                int id=stringToInt(input);
                Anime*result=db.getAnimeById(id);
                if(result){
                    result->displayFull();
                }else{
                    cout<<"Anime with ID "<<id<<" not found.\n"<<endl;
                }
                break;
            }
            case 3:{
                cout<<"Enter name to search: ";
                getline(cin,input);
                vector<Anime*>results=db.searchByName(input);
                if(!results.empty()){
                    cout<<"\nFound "<<results.size()<<" anime:\n";
                    cout<<string(115,'-')<<endl;
                    cout<<left<<setw(6)<<"ID"
                        <<setw(40)<<"Name"
                        <<setw(25)<<"Genre"
                        <<setw(8)<<"Year"
                        <<setw(8)<<"Rating"
                        <<setw(10)<<"Episodes"
                        <<setw(20)<<"Studio"<<endl;
                    cout<<string(115,'-')<<endl;
                    for(int i=0;i<results.size();i++){
                        results[i]->display();
                    }
                    cout<<string(115,'=')<<endl;
                }else{
                    cout<<"No anime found with name containing: "<<input<<"\n"<<endl;
                }
                break;
            }
            case 4:{
                cout<<"Enter genre to search: ";
                getline(cin,input);
                vector<Anime*>results=db.searchByGenre(input);
                if(!results.empty()){
                    cout<<"\nFound "<<results.size()<<" anime in genre '"<<input<<"':\n";
                    cout<<string(115,'-')<<endl;
                    cout<<left<<setw(6)<<"ID"
                        <<setw(40)<<"Name"
                        <<setw(25)<<"Genre"
                        <<setw(8)<<"Year"
                        <<setw(8)<<"Rating"
                        <<setw(10)<<"Episodes"
                        <<setw(20)<<"Studio"<<endl;
                    cout<<string(115,'-')<<endl;
                    for(int i=0;i<results.size();i++){
                        results[i]->display();
                    }
                    cout<<string(115,'=')<<endl;
                }else{
                    cout<<"No anime found in genre: "<<input<<"\n"<<endl;
                }
                break;
            }
            case 5:{
                cout<<"Enter studio to search: ";
                getline(cin,input);
                vector<Anime*>results=db.searchByStudio(input);
                if(!results.empty()){
                    cout<<"\nFound "<<results.size()<<" anime from studio '"<<input<<"':\n";
                    cout<<string(115,'-')<<endl;
                    cout<<left<<setw(6)<<"ID"
                        <<setw(40)<<"Name"
                        <<setw(25)<<"Genre"
                        <<setw(8)<<"Year"
                        <<setw(8)<<"Rating"
                        <<setw(10)<<"Episodes"
                        <<setw(20)<<"Studio"<<endl;
                    cout<<string(115,'-')<<endl;
                    for(int i=0;i<results.size();i++){
                        results[i]->display();
                    }
                    cout<<string(115,'=')<<endl;
                }else{
                    cout<<"No anime found from studio: "<<input<<"\n"<<endl;
                }
                break;
            }
            case 6:{
                Anime newAnime=getAnimeFromUser();
                db.addAnime(newAnime);
                break;
            }
            case 7:{
                cout<<"Enter ID to delete: ";
                getline(cin,input);
                int id=stringToInt(input);
                db.deleteAnime(id);
                break;
            }
            case 8:
                topAnimeMenu(db);
                break;
            case 9:
                db.displayStatistics();
                break;
            case 10:{
                cout<<"Enter filename (default: anime_data.txt): ";
                getline(cin,input);
                if(input.empty())input="anime_data.txt";
                db.loadFromFile(input);
                break;
            }
            case 11:{
                cout<<"Enter filename (default: anime_data.txt): ";
                getline(cin,input);
                if(input.empty())input="anime_data.txt";
                db.saveToFile(input);
                break;
            }
            case 12:{
                cout<<"Are you sure you want to clear the database? (y/n): ";
                getline(cin,input);
                if(input=="y"||input=="Y"){
                    db.clear();
                }else{
                    cout<<"Database not cleared.\n"<<endl;
                }
                break;
            }
            case 13:
                cout<<"\nTotal anime in database: "<<db.getCount()<<"\n"<<endl;
                break;
            case 0:
                cout<<"\nSaving data..."<<endl;
                db.saveToFile("anime_data.txt");
                cout<<"Thank you for using Anime Database!\n"<<endl;
                break;
            default:
                cout<<"Invalid choice! Please try again.\n"<<endl;
        }
        if(choice!=0){
            cout<<"Press Enter to continue...";
            getline(cin,input);
            cout<<"\n";
        }
    }while(choice!=0);
    return 0;
}