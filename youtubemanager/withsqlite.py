import sqlite3

con = sqlite3.connect('youtube_videos.db')
cursor = con.cursor()

cursor.execute('''
               CREATE TABLE IF NOT EXISTS videos(
                  id INTEGER PRIMARY KEY,
                  name TEXT NOT NULL,
                  time TEXT NOT NULL
                   )
               ''')

def listAllVideos():
    cursor.execute("SELECT * FROM videos")
    for row in cursor.fetchall():
        print(row)

def add_video(name, time):
    cursor.execute("INSERT INTO videos (name, time) VALUES (?, ?)", (name, time))
    con.commit()  # Corrected from cursor.commit() to con.commit()

def update_video(video_id, new_name, new_time):
    cursor.execute("UPDATE videos SET name=?, time=? WHERE id=?", (new_name, new_time, int(video_id)))
    con.commit()  # Corrected from cursor.commit() to con.commit()

def delete_video(video_id):
    cursor.execute("DELETE FROM videos WHERE id=?", (int(video_id),))
    con.commit()  # Corrected from cursor.commit() to con.commit()

def main():
    while True:
        print("\nYouTube manager app with DB")
        print("1. List Videos")
        print("2. Add videos")
        print("3. Update videos")
        print("4. Delete Videos")
        print("5. Exit app")
        choice = input("Enter your choice: ")

        match choice:
            case '1':
                listAllVideos()
            case '2':
                name = input("Enter the video name: ")
                time = input("Enter the video time: ")
                add_video(name, time)
            case '3':
                video_id = input("Enter video id to update: ")
                name = input("Enter the new video name: ")
                time = input("Enter the new video time: ")
                update_video(video_id, name, time)
            case '4':
                video_id = input("Enter video id to delete: ")
                delete_video(video_id)
            case '5':
                break
            case _:
                print("Invalid choice entered")
    
    con.close()

if __name__ == "__main__":
    main()
