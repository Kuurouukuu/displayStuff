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
		button {
			margin-bottom: 20px;
		}
	</style>
</head>
<body>
	<button id="toggleButton" onclick="toggleImages()">Hide Images</button>
	<div class="container">
		<img src="image1.png" alt="Image 1" width="300" height="200">
		<img src="image2.png" alt="Image 2" width="400" height="300">
		<img src="image3.png" alt="Image 3" width="500" height="400">
	</div>
	<script>
		function toggleImages() {
			const images = document.querySelectorAll('.image');
			images.forEach(image => {
				image.classList.toggle('hide');
				image.classList.toggle('show');
			});
			const button = document.querySelector('#toggleButton');
			if (button.innerHTML === 'Hide Images') {
				button.innerHTML = 'Show Images';
			} else {
				button.innerHTML = 'Hide Images';
			}
		}
	</script>
</body>
</html>
