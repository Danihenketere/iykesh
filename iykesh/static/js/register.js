const usernamefield = document.querySelector('#usernamefield');
const FeedbackArea = document.querySelector('.invalid-feedback');
const usernamecheck = document.querySelector('.usernamecheck');
const submitBtn = document.querySelector('.submit-btn');


usernamefield.addEventListener('keyup', (e)=>{
	
	const usernameVal = e.target.value;

	usernamefield.classList.remove('is-invalid');
	FeedbackArea.style.display = 'none';
	// usernamecheck.textContent = `checking ${usernameVal}`;

	if (usernameVal.length > 0 ){
		usernamecheck.textContent = `checking ${usernameVal}`;

		fetch('/authentication/validate-username', {
		body: JSON.stringify({ username: usernameVal }),
		method:'POST',
	}).then(res=>res.json()).then(data=>{

		if(data.username_error_message){
			submitBtn.disabled = true;
			usernamecheck.style.display = 'none'
			usernamefield.classList.add('is-invalid');
			FeedbackArea.style.display = 'block';
			FeedbackArea.innerHTML = `<p>${data.username_error_message}`;
		}else{
			submitBtn.disabled = false;
		}
		
		usernamecheck.style.display = 'block'
	});

	}


})


const emailfield = document.querySelector('#emailfield');
const eFeedbackArea = document.querySelector('.emailinvalid-feedback');
const emailcheck = document.querySelector('.emailcheck');

emailfield.addEventListener('keyup', (e)=>{
	
	const emailVal = e.target.value;

	emailfield.classList.remove('is-invalid');
	eFeedbackArea.style.display = 'none';

	if (emailVal.length > 0 ){
		// emailcheck.textContent = `checking ${emailVal}`;

		fetch('/authentication/validate-email', {
		body: JSON.stringify({ email: emailVal }),
		method:'POST',
	}).then(res=>res.json()).then(data=>{
		if(data.email_error_message){
			submitBtn.disabled = true;
			emailfield.classList.add('is-invalid');
			eFeedbackArea.style.display = 'block';
			eFeedbackArea.innerHTML = `<p>${data.email_error_message}`;
		}else{
			submitBtn.disabled = false;
		}
		// emailcheck.style.display = 'block'
	});

	}


})

const passwordtoggle = document.querySelector('.passwordtoggle');
const passwordfield = document.querySelector('#passwordfield');

const togglep = (e)=>{
	if (passwordtoggle.textContent === 'SHOW'){
		passwordfield.setAttribute('type', 'text')
		passwordtoggle.textContent = 'HIDE';
	}else{
		passwordfield.setAttribute('type', 'password')
		passwordtoggle.textContent = 'SHOW';
	}
}

passwordtoggle.addEventListener('click', togglep);

passwordfield.addEventListener('keyup', (e)=>{
	const passwordVal = e.target.value;
	if(passwordVal.length > 0){
		passwordtoggle.style.display = 'block';
		
	}else{
		passwordtoggle.style.display = 'none';
	}
});

