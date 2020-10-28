import instaloader
prof_name=input("Profile name: ")
x=instaloader.Instaloader()
x.download_profile(prof_name,profile_pic_only=True)