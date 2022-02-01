### TITLE PAGE ###
app = App(title="Login or Sign up")
text_blank = Text(app, text=" ")
text_blank = Text(app, text=" Welcome to ToKa Fitness ")
text_blank = Text(app, text=" ")
picture = Picture(app, image="homepage.jpg", height = 200, width = 400)
text_blank = Text(app, text=" ")
text_blank = Text(app, text=" ")

box1 = Box(app, layout = "grid", border = False)

login_button = PushButton(box1, text="Login", command = open_login, height = 1, width = 13, grid = [0,0])
login_button.bg = "light grey"
text_blank = Text(box1, text="              ", grid = [1,0])

signup_button = PushButton(box1, text = "Sign up", command = open_signup, height = 1, width = 13, grid = [2,0])
signup_button.bg = "light grey"

