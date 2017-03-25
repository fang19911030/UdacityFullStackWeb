/*
This is empty on purpose! Your code to build the resume will go here.
 */
 var work= {
 	"jobs":[{
 	"employer" : "Tianjin University",
 	"title" : "Research Assistant",
 	"location":"Tianjin, China",
 	"dates":"7/2014-12/2015",
 	"description":"Differentiated and monitored the complex movement patterns of multiphase flow. Published three papers about complex network analysis method cited more than 180 times."
 		}
 	]
 };
 var projects = {
 	"projects":[{
 		"title":"Application of support vector machine in classification of cancer patients",
 		"dates":"9/2016-12/2016",
 		"description":"Using different kinds biological and clinical data from the TCGA ( The Cancer Genome Atlas), buildt a predictor based on SVM to classify the patients(Metastasis or Not Metastasis).",
 		"images":[]
 	},
 	{
 		"title":"Development of human genetic interactions database based on the yeast-genetic interactions",
 		"dates":"9/2016-12/2016",
 		"description" :"Built the human genetic interactions database, according to the data of yeast-genetic interactions and homology genes of human and yeast.This database can be used to find special drugs for target genes of diseases.",
 		"images":["images/smallerData.jpg","images/smallerdata2.jpg"]
 	},
 	{
 		"title":"The remote monitor system based on the raspberry pi",
 		"dates":"3/2016-5/2016",
 		"description":"Developed a remote monitor system to process the ultrasonic signal and video input. Implemented the face-recognition function using openCV.",
 		"images":[]
 	},
 	{
 		"title":"The simulation of robotic simultaneous localization and mapping problem",
 		"dates":"2/2016-5/2016",
 		"description":"Built a simulator using A* algorithm and gradient decreasing algorithm to simulate the robot which can avoid the wall and the other obstacles.",
 		"images":["images/robot1.png","images/robot2.png"]
 	},
 	{
 		"title":"Development of complex network analytic tool for multiphase flow",
 		"dates":"7/2014-11/2015",
 		"description":"Successfully differentiated the various movement patterns of multiphase flow according to the analysis result of the data from electrical sensors .This analysis was based on the complex network theory.",
 		"images":[]

 	}
 	]
 };
 var bio={
 	"name" : "Pengcheng Fang",
 	"role" :"Full Stack Developer",
 	"skills" : ["Java","Python","SQL","NoSQL","HTML","JavaScript","CSS"],
 	"contacts":{
 		"email":"pxf109@case.edu",
 		"location":"Cleveland, OH, USA",
 		"blog" : "www.fangryan.com",
 		"github" :"fang1030",
 		"mobile":"216-666-0006"},
 	"biopic":"images/fry.jpg",
 	"welcomeMessage":"Welcome to my website"};
 var education={
 	"schools" :[
 	{"name":"Case Western University",
 	"location" :"Cleveland,OH,USA",
 	"majors":["Computer Science"],
 	"dates":"2018(anticipated)",
 	"url":"https://case.edu/"
 	},
 	{"name":"Tianjin University",
 	"location" :"Tianjin,China",
 	"majors":["Electrical Engineering and Computer Science"],
 	"dates":"2014",
 	"url":"http://www.tju.edu.cn/english/"
 	}
 	],
 	"onlineCourses":[
 	{
 		"title":"Introduction to Algorithms",
 		"school":"MIT",
 		"dates":"5/2016-9/2016",
 		"url":"https://ocw.mit.edu/courses/electrical-engineering-and-computer-science/6-006-introduction-to-algorithms-fall-2011/"
 	}
 	]
 };
 // if(document.getElementsByClassName("education-entry").length ===0){
 //      document.getElementById("education").style.backgroundColor="black";
 //    }
 //    if(document.getElementsByClassName("bio-entry").length ===0){
 //      document.getElementById("bio").style.backgroundColor="black";
 //    }
 //    if(document.getElementsByClassName("work-entry").length ===0){
 //      document.getElementById("work").style.backgroundColor="black";
 //    }
 //    if(document.getElementsByClassName("projects-entry").length ===0){
 //      document.getElementById("projects").style.backgroundColor="black";

$("#header").prepend(HTMLheaderName.replace("%data%",bio.name),HTMLheaderRole.replace("%data%",bio.role));
//$("#header").prepend(HTMLheaderRole.replace("%data%",bio.role));
$("#header").append(HTMLbioPic.replace("%data%",bio.biopic), HTMLwelcomeMsg.replace("%data%", bio.welcomeMessage));
//$("#header").append(HTMLbioPic.replace("%data%",bio.biopic));
var formattedMobil = HTMLmobile.replace("%data%",bio.contacts.mobile);
var formattedEmail = HTMLemail.replace("%data%",bio.contacts.email);
var formattedGithub = HTMLgithub.replace("%data%",bio.contacts.github);
var formattedLocation = HTMLlocation.replace("%data%",bio.contacts.location);
var formattedBlog = HTMLblog.replace("%data%",bio.contacts.blog);
$("#topContacts").append(formattedMobil,formattedEmail,formattedGithub,formattedBlog,formattedLocation);


if(bio.skills.length>0){
	$("#header").append(HTMLskillsStart);

	var formattedSkill = HTMLskills.replace("%data%",bio.skills[0]);
	//$("#skills").apend(formattedSkill);

	var formattedSkill2 =HTMLskills.replace("%data%",bio.skills[1]);
	//$("#skills").append(formattedSkill);
	var formattedSkill3 = HTMLskills.replace("%data%",bio.skills[2]);
	$("#skills").append(formattedSkill, formattedSkill2, formattedSkill3);
	formattedSkill = HTMLskills.replace("%data%",bio.skills[3]);
	$("#skills").append(formattedSkill);
	formattedSkill = HTMLskills.replace("%data%",bio.skills[4]);
	$("#skills").append(formattedSkill);
	formattedSkill = HTMLskills.replace("%data%",bio.skills[5]);
	$("#skills").append(formattedSkill);
	formattedSkill = HTMLskills.replace("%data%",bio.skills[6]);
	$("#skills").append(formattedSkill);

};
// for(job in work.jobs){
//   	$("#workExperience").append(HTMLworkStart);

//   	var formattedEmployer = HTMLworkEmployer.replace("%data%", work.jobs[job].employer);
//   	var formattedTitle = HTMLworkTitle.replace("%data%",work.jobs[job].title);
//   	var formattedEmployerTitle = formattedEmployer + formattedTitle;
//   	$(".work-entry:last").append(formattedEmployerTitle);
//   	var formattedDate = HTMLworkDates.replace("%data%",work.jobs[job].dates);
//   	$(".work-entry:last").append(formattedDate);
//  	var formattedLocation = HTMLworkLocation.replace("%data%",work.jobs[job].location);
//   	$(".work-entry:last").append(formattedLocation);
//  	var formattedDescription = HTMLworkDescription.replace("%data%",work.jobs[job].description);
//   	$(".work-entry:last").append(formattedDescription);
//   };

  function displayWork(){
  	for(job in work.jobs){
  		$("#workExperience").append(HTMLworkStart);

  		var formattedEmployer = HTMLworkEmployer.replace("%data%", work.jobs[job].employer);
  		var formattedTitle = HTMLworkTitle.replace("%data%",work.jobs[job].title);
  		var formattedEmployerTitle = formattedEmployer + formattedTitle;
  		$(".work-entry:last").append(formattedEmployerTitle);
  		var formattedDate = HTMLworkDates.replace("%data%",work.jobs[job].dates);
 		$(".work-entry:last").append(formattedDate);
  		var formattedLocation = HTMLworkLocation.replace("%data%",work.jobs[job].location);
  		$(".work-entry:last").append(formattedLocation);
  		var formattedDescription = HTMLworkDescription.replace("%data%",work.jobs[job].description);
		$(".work-entry:last").append(formattedDescription);
	}

  };
 displayWork();

projects.display = function(){
	for(project in projects.projects){
		$("#projects").append(HTMLprojectStart);
		var formattedProjectTitle = HTMLprojectTitle.replace("%data%",projects.projects[project].title);
		var formattedProjectDate = HTMLprojectDates.replace("%data%",projects.projects[project].dates);
		var formattedProjectDes = HTMLprojectDescription.replace("%data%",projects.projects[project].description);

		
		$(".project-entry:last").append(formattedProjectTitle);
		$(".project-entry:last").append(formattedProjectDate);
		$(".project-entry:last").append(formattedProjectDes);
		if(projects.projects[project].images.length>0){
			for( image in projects.projects[project].images){
				var formattedProjectPic = HTMLprojectImage.replace("%data%",projects.projects[project].images[image]);
				$(".project-entry:last").append(formattedProjectPic);

			};

		};
		
	};
 };
projects.display();
education.display = function(){
	for (school in education.schools){
		$("#education").append(HTMLschoolStart);
		var formattedSchoolName = HTMLschoolName.replace("%data%",education.schools[school].name);
		var formattedSchoolLocation = HTMLschoolLocation.replace("%data%", education.schools[school].location)
		var formattedSchoolMajor = HTMLschoolMajor.replace("%data%",education.schools[school].majors[0]);
		var formattedSchoolDated = HTMLschoolDates.replace("%data%",education.schools[school].dates);
		$(".education-entry:last").append(formattedSchoolName);
		$(".education-entry:last").append(formattedSchoolLocation);
		$(".education-entry:last").append(formattedSchoolMajor);
		$(".education-entry:last").append(formattedSchoolDated);
	};

};
education.display();
$(document).click(function(loc){
	var x = loc.pageX ;
	var y = loc.pageY;
	logClicks(x, y);
});


