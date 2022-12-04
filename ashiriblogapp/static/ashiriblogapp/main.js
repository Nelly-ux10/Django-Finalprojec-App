//console.dir(document);
//hover over effects on the different commumities
function bigImg(x) {
  x.style.height = "75px";
  x.style.width = "120px";
}

function normalImg(x) {
  
  x.style.width = "90px";
}
//second community
function bigImg1(x) {
  x.style.height = "75px";
  x.style.width = "120px";
}

function normalImg1(x) {
  
  x.style.width = "90px";
}
//third community
function bigImg2(x) {
  x.style.height = "75px";
  x.style.width = "120px";
}

function normalImg2(x) {
  
  x.style.width = "90px";
}

//click on the add button to see the effect
function img_increase()
        {
            document.getElementById("img1").style.width="200px";
						document.getElementById("img1").style.backgroundColor = "yellow";
 				
        } 

        function img_decrease()
        {
          document.getElementById("img1").style.width="100px";
					document.getElementById("img1").style.backgroundColor = "rgb(231, 205, 205)"; 
        }

// for the form sumbit
//const form = document.getElementById('login');
//const fname = document.getElementById('fname');
//const lname = document.getElementById('lname');
//const uname = document.getElementById('uname');
//const pswd = document.getElementById('pswd');
//const cpswd = document.getElementById('cpswd');
//const email = document.getElementById('email');

//form.addEventListener('submit', (e) => {
		//e.preventDefault();

		//checkInputs();
//});

//function checkInputs(){
// get values from our imputs
		//const fnameValue = fname.value.trim(); // using trim to remove white spaces
		//const lnamevalue = lname.value.trim();
		//const unamevalue =  uname.value.trim();
		//const emailvalue =  email.value.trim();
		//const pswdvalue =  pswd.value.trim();
		//const cpswdvalue = cpswd.value.trim();

		//if(fnameValue === '' ){
				//show error
				//add error class
				//setErrorFor(fname, 'first name can not be empty');
			//} else{
			//add success class
			//setSuccessFor(fname);
			//}
//}

//function setErrorFor(input, message){
		//const formInputGroup = input.parentElement;//
		//const small = formInputGroup.querySelector('small');
		//add error 
		//small.innerText = message;
		

		//add error class
	//	formInputGroup.className = 'formInputGroup error';
//}

// funtion for submit signup form
$("#login input").on("input",function(){
	$("#full-name").val($("#fname").val()+" "+$("#lname").val());
});