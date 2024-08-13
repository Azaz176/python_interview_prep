import json

def load_data():
    try:
        with open('youtube.txt', 'r') as file:
            test=json.load(file)
            print(type(test))
            return test
    except FileNotFoundError:
        return []

def save_data_helper(videos):
    with open('youtube.txt', 'w') as file:
        json.dump(videos, file)       
    
def listAllVideos(videos):
    print("\n")
    print("*"*72)
    for index, video in enumerate(videos, start=1):
        
        print(f"{index}. {video['name']}, Duration:{video['time']}")
    print("\n")
    print("*"*72)
def add_video(videos):
    name=input("Enter video name:")
    time= input("Enter video time:")
    videos.append({'name':name, 'time':time})
    save_data_helper(videos)
def update_video(videos):
    listAllVideos(videos)
    index= int(input("Enter the video number to update"))
    if 1<=index <= len(videos):
        name=input("Enter the new video name")
        time=input("Enter the new video time")
        videos[index-1]={'name':name, 'time':time}
        save_data_helper(videos)
    else:
        print("invalid index selected")
def delete_video(videos):
    listAllVideos(videos)
    index=int(input("Enter the video number to be deleted"))
    if 1<=index<=len(videos):
        del videos[index-1]
        save_data_helper(videos)
    else:
        print("invalid video selected")

def main():
    videos= load_data()
    while True:
        print("\n Youtube manager, choose an option")
        print("1. list of favorite videos")
        print("2. Add a youtube video")
        print("3. update a youtube video detals")
        print("4. delete a youtube video")
        print("5. exit the app")
        choice= input("enter your choice:")
        # print(videos)
        match choice:
            case '1':
                listAllVideos(videos)
            case '2':
                add_video(videos)
            case '3':
                update_video(videos)
            case '4':
                delete_video(videos)
            case '5':
                break
            case _:
                print("Invalid choice entered")
        

if __name__ == "__main__":
    main()