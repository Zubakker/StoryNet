function press_like(comment_id) {
	let like_button_obj = document.getElementById('like_button_obj' + comment_id);
	let like_number_obj = document.getElementById('like_number_obj' + comment_id);
	if (like_button_obj.style.backgroundImage == 'url("' + unliked_img_url + '")') {
		like_button_obj.style.backgroundImage = 'url("' + liked_img_url + '")'; 
		like_number_obj.innerHTML = parseInt(like_number_obj.innerHTML) + 1;
	}
	else {
		like_button_obj.style.backgroundImage = 'url("' + unliked_img_url + '")';
		like_number_obj.innerHTML = parseInt(like_number_obj.innerHTML) - 1;
	}
	request_like(comment_id);
	return;

}
function request_like(comment_id) {
	let get_req = new XMLHttpRequest();
	get_req.open('GET', comments_url + '?like=' + comment_id, true);

	get_req.onload = function () {
		result = JSON.parse(get_req.responseText);
		console.log(result);
	};

	get_req.send(null);
	return;
}
function comments_more() {

	let get_req = new XMLHttpRequest();
	get_req.open('GET', comments_url + '?page=' + page_num, true);
	page_num += 1;

	get_req.onload = function () {
		comment_list = JSON.parse(get_req.responseText);
		comment_list_obj = document.getElementById('custom_comments_obj');
		for (let comment_obj of comment_list) {
			let added_text = `
		<div class='comment_list_item'>
			<div class='comment_tagline'>
				<b class='full_name'>
					<a href='${ comment_obj["url"] }' class='author_name_link'>
						 ${ comment_obj["author"] }
					</a>
				</b>
				<div class='time_created'>
					${ comment_obj["created_at"] }
				</div>
			</div>
			<div class='text_like'>
				<p class='comment_text'>${ comment_obj["text"] }</p>
				<div class='like_full'>
					<button 
					 	class='like_button'
						id='like_button_obj${ comment_obj["id"] }'
						style='background-image:` 
			if (comment_obj["ILiked"]){
				added_text += 'url("' + liked_img_url + `")'`;
			}
			else {
				added_text += 'url("' + unliked_img_url + `")'`;
			}
			added_text += `
					 	onclick='press_like(${ comment_obj["id"] })'
					>
					</button>
					<span id='like_number_obj${ comment_obj["id"] }'>${ comment_obj["like_number"] }</span>
				</div>
			</div>
		</div>
		`;
			comment_list_obj.innerHTML += added_text;
		};
	}
	get_req.send(null);
}
function scroll_handler() {
	let vertical_scroll = window.scrollY;
	document_height = document.body.clientHeight;
	window_height = window.innerHeight;
	bottom_coords = document_height - window_height;
	if (vertical_scroll > (bottom_coords - 20)) { // we leave some room bc vertical scroll might be a little off
		comments_more();
	}
}
