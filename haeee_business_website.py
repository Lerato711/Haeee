import zipfile
import os

# Create directory structure
os.makedirs('haeee-website/css', exist_ok=True)
os.makedirs('haiye-website/images', exist_ok=True)
os.makedirs('haiye-website/js', exist_ok=True)

# Create index.html
with open('haiye-website/index.html', 'w') as f:
    f.write("""<!DOCTYPE html>
<html lang='en'>
<head>
<meta charset='UTF-8'>
<meta name='viewport' content='width=device-width, initial-scale=1.0'>
<title>Haiye - Online Marketplace & Courier</title>
<link rel='stylesheet' href='css/style.css'>
</head>
<body>
<header>
<div class='container'>
<h1 class='logo'>Haiye</h1>
<nav>
<ul>
<li><a href='index.html'>Home</a></li>
<li><a href='about.html'>About Us</a></li>
<li><a href='services.html'>Services</a></li>
<li><a href='contact.html'>Contact</a></li>
</ul>
</nav>
</div>
</header>
<section class='hero'>
<div class='container'>
<h2>Welcome to Haiye</h2>
<p>Your one-stop online marketplace & fast courier service.</p>
<a href='services.html' class='btn'>Explore Services</a>
</div>
</section>
<section class='features'>
<div class='container'>
<div class='feature-box'>
<h3>Online Marketplace</h3>
<p>Buy and sell products easily on Haiye’s platform.</p>
</div>
<div class='feature-box'>
<h3>Courier Service</h3>
<p>Fast and reliable delivery across cities and countries.</p>
</div>
</div>
</section>
<footer>
<div class='container'>
<p>&copy; 2026 Haiye. All rights reserved.</p>
</div>
</footer>
</body>
</html>""")

# Create other HTML files
html_files = ['about.html', 'services.html', 'contact.html']
html_contents = ['about', 'services', 'contact']
for file, content in zip(html_files, html_contents):
    with open(f'haiye-website/{file}', 'w') as f:
        f.write(f"<!DOCTYPE html>\n<html lang='en'>\n<head>\n<meta charset='UTF-8'>\n<meta name='viewport' content='width=device-width, initial-scale=1.0'>\n<title>{content.capitalize()} - Haiye</title>\n<link rel='stylesheet' href='css/style.css'>\n</head>\n<body>\n<header>\n<div class='container'>\n<h1 class='logo'>Haiye</h1>\n<nav>\n<ul>\n<li><a href='index.html'>Home</a></li>\n<li><a href='about.html'>About Us</a></li>\n<li><a href='services.html'>Services</a></li>\n<li><a href='contact.html'>Contact</a></li>\n</ul>\n</nav>\n</div>\n</header>\n<section class='{content}'>\n<div class='container'>\n<h2>{content.capitalize()}</h2>\n<p>Content for the {content} page goes here.</p>\n</div>\n</section>\n<footer>\n<div class='container'>\n<p>&copy; 2026 Haiye. All rights reserved.</p>\n</div>\n</footer>\n</body>\n</html>")

# Create style.css
style_css = """/* CSS content here */ body{font-family:Arial,sans-serif;}"""
with open('haiye-website/css/style.css', 'w') as f:
    f.write(style_css)

# Create zip file
with zipfile.ZipFile('haiye-website.zip', 'w') as zipf:
    for root, dirs, files in os.walk('haiye-website'):
        for file in files:
            zipf.write(os.path.join(root, file))

'haiye-website.zip created successfully'
