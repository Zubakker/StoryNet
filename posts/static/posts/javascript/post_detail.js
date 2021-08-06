let page_array = [];
let page_number = -1;
function pofig() {
	let padding_side = 20;

	let padding_top = 20;
	let max_line_len = 45;
	let max_line_num = 23;

	let text_obj = document.getElementById('text_obj');
	let page_obj = document.getElementById('page_obj');
	let width = page_obj.offsetWidth;
	let height = page_obj.offsetHeight;
	
	
	// let current_line = '';
	// let current_page = '';
	// let line_number = 0;
	
	let current_page = '';
	let dcurrent_page = '';
	for (let word of post_text) {
		dcurrent_page += word + ' ';
		page_obj.innerHTML = dcurrent_page;
		let dheight = page_obj.offsetHeight;
		if (dheight <= height) {
			current_page += word + ' ';
		}
		else {
			page_array.push(current_page);
			current_page = word + ' ';
			dcurrent_page = word + ' ';
		}
	}
	
	// for (let word of text) {
		// if (word.length + current_line.length <= max_line_len) {
			// current_line += word + ' ';
		// }
		// else {
			// current_page += current_line + '\n';
			// line_number += 1;
			// current_line = '';
			// if (line_number == max_line_num) {
				// page_array.push(current_page);
				// current_line = '';
				// current_page = '';
				// line_number = 0;
			// }
		// }
	// }
	page_array.push(current_page);
	title_page();
	return;
}
function next_page() {
	page_number += 1; 
	if (page_number >= page_array.length) {
		page_number = page_array.length - 1;
	}
	let page_obj = document.getElementById('page_obj');
	page_obj.innerHTML = page_array[ page_number ];
	return;
}
function previous_page() {
	page_number -= 1; 
	if (page_number < 0) {
		title_page();
		page_number = -1;
		return;
	}
	let page_obj = document.getElementById('page_obj');
	page_obj.innerHTML = page_array[ page_number ];
	return;
}
function title_page() {
	let page_obj = document.getElementById('page_obj');
	page_obj.innerHTML = 'первая страница';
	return;
}
