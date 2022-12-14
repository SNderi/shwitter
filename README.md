# SHWITTER
Shwitter is a social media application that is used to share text based messageswith the world.
You can follow or unfollow any subscribers to see their shweets as well as share your thoughts with them.

![alt text](https://github.com/SNderi/shwitter/blob/main/Images/dashboard.png)

## Explore Shwitter
### Installation and Usage
```bash
# Clone this repository
$ git clone https://github.com/SNderi/shwitter.git`

# Go into the repository
$ cd shwitter/shwitter`

# Run the application server
$ python3 manage.py runserver`
```

Navigate to `http://127.0.0.1:8000/` on your web browser and explore shwitter using the different profiles already registered.
You can read and post shweets, follow or unfollow profiles, see a list of profiles following you as well as those you are following and view all user profiles.

## Architecture
https://github.com/SNderi/shwitter/blob/main/Images/architecture.png

## API's
- /shwitter/profile_list
GET: Returns a list of all the users with their profiles.
- /shwitter/profile/id
GET: Returns unique id profile

## Shwitter Views
https://github.com/SNderi/shwitter/blob/main/Images/profile_list.png
https://github.com/SNderi/shwitter/blob/main/Images/profile.png

## Languages Libraries and Frameworks used
- Python
- HTML
- CSS
- Django
- Bulma
- SQLite

## Authors
> [William Mwangi](./https://github.com/william-4)
> [Sharon Nderi](./https://github.com/SNderi)
