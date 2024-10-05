1) Clone this repo
2) create venv: **python -m venv myvenv**
3) **pip install -r requirements.txt**
4) run **docker compose up --build -d**
5) rename .env.template to .env
6) go to cats_website/ folder and run **pytest**

Swagger doc is available at http://127.0.0.1:1337/schema/swagger-ui/

Prepopulated data:
1)Superuser: 
  username: admin
  password: admin
2) Users:
  1) username: user1
     password: password1
  2) username: user2
     password: password2
3) I also added Breeds and Cats, see admin panel 
