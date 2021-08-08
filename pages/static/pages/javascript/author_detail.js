let true_bio_text = '';
let true_cont_text= '';
function shorter() {
	let about_obj = document.getElementById('about-obj');
	let bio_obj = document.getElementById('bio-obj');
	let cont_obj = document.getElementById('cont-obj');

	// bio_text = bio_obj.innerHTML;
	bio_obj.innerHTML = 'О себе:<br>'
	test_bio_text = '';
	true_bio_text = '';

	// cont_text = cont_obj.innerHTML;
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

function posts_more() {

	let get_req = new XMLHttpRequest();
	get_req.open('GET', '/author/1?page=' + page_num, true);
	page_num += 1;

	get_req.onload = function () {
		console.log(get_req.responseText);
		post_list = JSON.parse(get_req.responseText);
		post_list_obj = document.getElementById('post_list');
		for (let post_obj of post_list) {
			let added_text = '';
			if (post_obj['long']) {
				added_text = '...';
			}
			console.log(post_obj["text"]);
			post_list_obj.innerHTML += `
			<div class='post_list_item'>
				<b><a href='${post_obj["url"]}' class='title_link'>${post_obj["title"]}</a></b>
				<p>${post_obj["text"]}
					${added_text}
				</p>
			<div>`;
		}
	};

	get_req.send(null);
}
function scroll_handler() {
	let vertical_scroll = window.scrollY;
	document_height = document.body.clientHeight;
	window_height = window.innerHeight;
	bottom_coords = document_height - window_height;
	if (vertical_scroll > (bottom_coords - 20)) { // we leave some room bc vertical scroll might be a little off
		posts_more();
	}
}
