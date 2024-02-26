const x = document.querySelector("#myTopnav");
const y  = document.querySelector(".icon");
		
		
y.onclick = ()=>{
  
if(x.className === "menu-bar"){
      x.className += " responsive";
}else{
        x.className = "menu-bar";
}
}

var counter = 1;
setInterval(function(){
	document.getElementById('radio' + counter).checked = true;
	counter++;
	if(counter > 5){
		counter = 1;
	}
	
}, 5000);


// ..........This codes below takes care of image file selection.......
const inpFile = document.getElementById("inpFile");
const previewContainer = document.getElementById("imagePreview");
const previewImage = previewContainer.querySelector(".image-preview__image");
const previewDefaultText = previewContainer.querySelector(".image-preview__default-text");


inpFile.addEventListener('change', function(){
	const file = this.files[0];
	if(file){
		const reader = new FileReader()

		previewDefaultText.style.display = 'none';
		previewImage.style.display = 'block';


		reader.addEventListener('load', function(){
			previewImage.setAttribute('src', this.result);
		});

		reader.readAsDataURL(file);
	}else{
		previewDefaultText.style.display = null;
		previewImage.style.display = null;
		previewImage.setAttribute('src', "");
	}
});


const inpFile1 = document.getElementById("inpFile1");
const previewContainer1 = document.getElementById("imagePreview1");
const previewImage1 = previewContainer1.querySelector(".image-preview__image1");
const previewDefaultText1 = previewContainer1.querySelector(".image-preview__default-text");


inpFile1.addEventListener('change', function(){
	const file1 = this.files[0];
	if(file1){
		const reader1 = new FileReader()

		previewDefaultText1.style.display = 'none';
		previewImage1.style.display = 'block';


		reader1.addEventListener('load', function(){
			previewImage1.setAttribute('src', this.result);
		});

		reader1.readAsDataURL(file1);
	}else{
		previewDefaultText1.style.display = null;
		previewImage1.style.display = null;
		previewImage1.setAttribute('src', "");
	}
});

const inpFile2 = document.getElementById("inpFile2");
const previewContainer2 = document.getElementById("imagePreview2");
const previewImage2 = previewContainer2.querySelector(".image-preview__image2");
const previewDefaultText2 = previewContainer2.querySelector(".image-preview__default-text");


inpFile2.addEventListener('change', function(){
	const file2 = this.files[0];
	if(file2){
		const reader2 = new FileReader()

		previewDefaultText2.style.display = 'none';
		previewImage2.style.display = 'block';


		reader2.addEventListener('load', function(){
			previewImage2.setAttribute('src', this.result);
		});

		reader2.readAsDataURL(file2);
	}else{
		previewDefaultText2.style.display = null;
		previewImage2.style.display = null;
		previewImage2.setAttribute('src', "");
	}
});

const inpFile3 = document.getElementById("inpFile3");
const previewContainer3 = document.getElementById("imagePreview3");
const previewImage3 = previewContainer3.querySelector(".image-preview__image3");
const previewDefaultText3 = previewContainer3.querySelector(".image-preview__default-text");


inpFile3.addEventListener('change', function(){
	const file3 = this.files[0];
	if(file3){
		const reader3 = new FileReader()

		previewDefaultText3.style.display = 'none';
		previewImage3.style.display = 'block';


		reader3.addEventListener('load', function(){
			previewImage3.setAttribute('src', this.result);
		});

		reader3.readAsDataURL(file3);
	}else{
		previewDefaultText3.style.display = null;
		previewImage3.style.display = null;
		previewImage3.setAttribute('src', "");
	}
});

const inpFile4 = document.getElementById("inpFile4");
const previewContainer4 = document.getElementById("imagePreview4");
const previewImage4 = previewContainer4.querySelector(".image-preview__image4");
const previewDefaultText4 = previewContainer4.querySelector(".image-preview__default-text");


inpFile4.addEventListener('change', function(){
	const file4 = this.files[0];
	if(file4){
		const reader4 = new FileReader()

		previewDefaultText4.style.display = 'none';
		previewImage4.style.display = 'block';


		reader4.addEventListener('load', function(){
			previewImage4.setAttribute('src', this.result);
		});

		reader4.readAsDataURL(file4);
	}else{
		previewDefaultText4.style.display = null;
		previewImage4.style.display = null;
		previewImage4.setAttribute('src', "");
	}
});




	
	var s1 = document.getElementById('slct1');
	var s2 = document.getElementById('slct2');
	var s3 = document.getElementById('slctd');
	var s4 = document.getElementById('slctd1');
	var s5 = document.getElementById('slctd2');
	var s6 = document.getElementById('slctd3');
	s1.onchange = ()=>{
		
	s2.innerHTML = '';

	if(s1.value == "Material"){
		var optionArray = ["|", "fabric|Fabric", "leather|Leather", "leather-fabric|Leather-Fabric"];
	}else if(s1.value == "Foam"){
		var optionArray = ["|", "naked|Naked", "pieces|Pieces", "covered|Covered"];
	}else if(s1.value == "Tool"){
		var optionArray = ["|", "hammer|Hammer", "scissors|Scissors", "stapler|Stapeler", "pinches|Pinches", "sewing Machine|Sewing Machine"];
	}else 	if(s1.value == "Wood"){
		var optionArray = ["|", "wood|Wood", "nails|Nails", "chairleg|Chairleg", "rubber|Rubber", "skeleton|Skeleton", "rope|Rope", "wools|Wools", "niddles|Niddles", "buttons|Buttons"];
	}
	for(var option in optionArray){
		var pair = optionArray[option].split("|");
		var newOption = document.createElement("option");
		newOption.value = pair[0];
		newOption.innerHTML = pair[1];
		s2.options.add(newOption);

	}
	s3.value = s1.value;

}

	s2.onchange = ()=>{
		
	s4.value = s2.value;
}
	s5.onchange = ()=>{
		
	s6.value = s5.value;
}

// Product page script
var productImg =document.getElementById("product-img");
var smallImg =document.getElementsByClassName("small-img");
console.log(smallImg[0])
smallImg[0].onclick = function(){
	productImg.src = smallImg[0].src;
}
smallImg[1].onclick = ()=>{
	productImg.src = smallImg[1].src;
}
smallImg[2].onclick = ()=>{
	productImg.src = smallImg[2].src;
}
smallImg[3].onclick = ()=>{
	productImg.src = smallImg[3].src;
}
smallImg[4].onclick = ()=>{
	productImg.src = smallImg[4].src;
}