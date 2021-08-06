let bio_text = '';
let true_bio_text = '';
let cont_text = '';
let true_cont_text= '';
function shorter() {
	let about_obj = document.getElementById('about-obj');
	let bio_obj = document.getElementById('bio-obj');
	let cont_obj = document.getElementById('cont-obj');

	bio_text = bio_obj.innerHTML;
	bio_obj.innerHTML = 'О себе:<br>'
	test_bio_text = '';
	true_bio_text = '';

	cont_text = cont_obj.innerHTML;
	cont_obj.innerHTML = 'Контакты:<br>'
	test_cont_text = '';
	true_cont_text = '';

	let about_height = about_obj.offsetHeight;

	for (let word of bio_text.split(' ')) {
		test_bio_text += word + '<br><br>';
		bio_obj.innerHTML = test_bio_text;
		if (about_obj.offsetHeight <= about_height) {
			true_bio_text += word + ' ';
			test_bio_text = true_bio_text;
		}
		else {
			bio_obj.innerHTML = true_bio_text + '<br><button class="more_button" onclick="bio_more()">полностью</button>';
			break;
		}
	}
	for (let word of cont_text.split(' ')) {
		test_cont_text += word + '<br><br>';
		cont_obj.innerHTML = test_cont_text;
		if (about_obj.offsetHeight <= about_height) {
			true_cont_text += word + ' ';
			test_cont_text = true_cont_text;
		}
		else {
			cont_obj.innerHTML = true_cont_text + '<br><button class="more_button" onclick="cont_more()">полностью</button>';
			break;
		}
	}
	return;
}
function bio_more() {
	let bio_obj = document.getElementById('bio-obj');
	bio_obj.innerHTML = bio_text + '<br><button class="more_button" onclick="bio_less()">скрыть</a>'
}
function bio_less() {
	let bio_obj = document.getElementById('bio-obj');
	bio_obj.innerHTML = true_bio_text + '<br><button class="more_button" onclick="bio_more()">полностью</a>'
}
function cont_more() {
	let cont_obj = document.getElementById('cont-obj');
	cont_obj.innerHTML = cont_text + '<br><button class="more_button" onclick="cont_less()">скрыть</a>'
}
function cont_less() {
	let cont_obj = document.getElementById('cont-obj');
	cont_obj.innerHTML = true_cont_text + '<br><button class="more_button" onclick="cont_more()">скрыть</a>'
}
