import zipfile
import os

# Create directory structure
os.makedirs('haeee-website/css', exist_ok=True)
os.makedirs('haeee-website/images', exist_ok=True)
os.makedirs('haeee-website/js', exist_ok=True)

# Create index.html
with open('haeee-website/index.html', 'w') as f:
    f.write("""<!DOCTYPE html>
<html lang='en'>
<head>
<meta charset='UTF-8'>
<meta name='viewport' content='width=device-width, initial-scale=1.0'>
<title>Haeee - Online Marketplace & Courier</title>
<link rel='stylesheet' href='css/style.css'>
</head>
<body>
<header>
<div class='container'>
<h1 class='logo'>Haeee</h1>
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
<h2>Welcome to Haeee</h2>
<p>Your one-stop online marketplace & fast courier service.</p>
<a href='services.html' class='btn'>Explore Services</a>
</div>
</section>
<section class='features'>
<div class='container'>
<div class='feature-box'>
<h3>Online Marketplace</h3>
<p>Buy and sell products easily on Haeee’s platform.</p>
</div>
<div class='feature-box'>
<h3>Courier Service</h3>
<p>Fast and reliable delivery across cities and countries.</p>
</div>
</div>
</section>
<footer>
<div class='container'>
<p>&copy; 2026 Haeee. All rights reserved.</p>
</div>
</footer>
</body>
</html>"""

# Create other HTML files
html_files = ['about.html', 'services.html', 'contact.html']
html_contents = ['about', 'services', 'contact']
for file, content in zip(html_files, html_contents):
    with open(f'haeee-website/{file}', 'w') as f:
        f.write(f"""<!DOCTYPE html>
<html lang='en'>
<head>
<meta charset='UTF-8'>
<meta name='viewport' content='width=device-width, initial-scale=1.0'>
<title>{{content.capitalize()}} - Haeee</title>
<link rel='stylesheet' href='css/style.css'>
</head>
<body>
<header>
<div class='container'>
<h1 class='logo'>Haeee</h1>
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
<main class='container'>
<h2>{{content.capitalize()}}</h2>
<p>This is the {{content}} page for Haeee.</p>
</main>
<footer>
<div class='container'>
<p>&copy; 2026 Haeee. All rights reserved.</p>
</div>
</footer>
</body>
</html>""")

# Create style.css
style_css = """/* CSS content here */ body{font-family:Arial,sans-serif;}"""
with open('haeee-website/css/style.css', 'w') as f:
    f.write(style_css)

# Create zip file
with zipfile.ZipFile('haeee-website.zip', 'w') as zipf:
    for root, dirs, files in os.walk('haeee-website'):
        for file in files:
            zipf.write(os.path.join(root, file))

'haeee-website.zip created successfully'