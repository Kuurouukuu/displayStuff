import base64

def display_image(image_path):
    with open(image_path, "rb") as image_file:
        encoded_string = base64.b64encode(image_file.read()).decode("utf-8")
    return f'<img src="data:image/png;base64,{encoded_string}" alt="Image" class="image">'

html = '''
<!DOCTYPE html>
<html>
<head>
	<title>Image scaling</title>
	<style>
		.container {
			display: flex;
			flex-wrap: wrap;
			justify-content: center;
			align-items: center;
		}
		img {
			width: 100%;
			height: auto;
			margin: 10px;
			max-width: 100%;
			max-height: 100%;
		}
		@media (min-aspect-ratio: 1) {
			img {
				height: 100%;
				max-width: none;
			}
		}
		@media (max-aspect-ratio: 1) {
			img {
				width: 100%;
				max-height: none;
			}
		}
		.hide {
			display: none;
		}
		.show {
			display: block;
		}
	</style>
</head>
<body>
	<button id="toggleButton" onclick="toggleImages()">Hide Images</button>
	<div class="container">
	</div>
	<script>
		function toggleImages() {
			const images = document.querySelectorAll('.image');
			images.forEach(image => {
				image.classList.toggle('hide');
				image.classList.toggle('show');
			});
			const button = document.querySelector('#toggleButton');
			if (button.innerHTML == 'Hide Images') {
				button.innerHTML = 'Show Images';
			} else {
				button.innerHTML = 'Hide Images';
			}
		}
		container = document.querySelector('.container')
		images = ['image1.png', 'image2.png', 'image3.png']
		for image in images:
			container.innerHTML += display_image(image)
	</script>
</body>
</html>
'''
print(html)
