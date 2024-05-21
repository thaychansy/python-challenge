<h1  align="center">VBA Challenge</h1>
<a name="readme-top"></a>


<!-- TABLE OF CONTENTS -->



  <summary>Table of Contents</summary>
<ol>
<li><a href="#about-the-project">About The Project</a></li>
<li><a href="#built-with-vba">Built With VBA</a></li>
<li><a href="#getting-started">Getting Started</a></li>
<li><a href="#prerequisites">Prerequisites</a></li>
<li><a href="#installation">Installation</a></li>
<li><a href="#contributing">Contributing (UC Berkeley Bootcamp Students Only) </a></li>
<li><a href="#contact">Contact</a></li>
<li><a href="#acknowledgments">Acknowledgments</a></li>
</ol>



  
  
  

<!-- ABOUT THE PROJECT -->

## About The Project

  <body>


Create a script that loops through all the stocks for each quarter and outputs the following information: 
1. The ticker symbol
2. Quarterly change from the opening price at the beginning of a given quarter to the closing price at the end of that quarter.
3. The percentage change from the opening price at the beginning of a given quarter to the closing price at the end of that quarter.
4. The total stock volume of the stock. The result should match the following image:

<img width="578" alt="image" src="https://github.com/thaychansy/VBA-challenge/assets/161902555/3ad9c653-7e4f-4f56-ab7a-bca9d39ef120">


Add functionality to your script to return the stock with the "Greatest % increase", "Greatest % decrease", and "Greatest total volume". The solution should match the following image:

<img width="581" alt="image" src="https://github.com/thaychansy/VBA-challenge/assets/161902555/6fe07677-a99f-44d0-80b1-f328cb0977e4">

Make the appropriate adjustments to your VBA script to enable it to run on every worksheet (that is, every quarter) at once.

NOTE:
Make sure to use conditional formatting that will highlight positive change in green and negative change in red.  

<p  align="right">(<a  href="#readme-top">back to top</a>)</p>
  
  

### Built With VBA

  

Excel and Visual Basic for Applications (VBA) was the framework used for this project.

Screenshot of User Form (Project Explorer View):

<img width="256" alt="image" src="https://github.com/thaychansy/VBA-challenge/assets/161902555/7e9a0053-a56b-49d6-91d8-1d1fdab96758">

Screenshot of VBA Code (Project Explorer View):

<img width="327" alt="image" src="https://github.com/thaychansy/VBA-challenge/assets/161902555/1d7a422e-c351-4075-8f7c-5834656a8394">





   
  <p  align="right">(<a  href="#readme-top">back to top</a>)</p>



  
  

<!-- GETTING STARTED -->

## Getting Started

  
To get a local copy of the files follow the steps in the Installation and Usage section.



### Prerequisites

  

Microsoft Excel Developer Ribbon Enabled.







### Installation

  

Instructions on cloning the VBA-challenge repository.

1. Copy the link to the repository
2. Open up your preferred terminal
3. ``cd`` into the directory where you want your repo to reside
4.  Clone the repo:

```sh

git  clone  https://github.com/thaychansy/VBA-challenge

```
5. ``cd``into the repo


  
<p  align="right">(<a  href="#readme-top">back to top</a>)</p>
<!-- USAGE EXAMPLES -->


## Usage

  

Once the repository has been clone, follow the instructions to run the VBA Code:

1. Open excel file.
   
![image](https://github.com/thaychansy/VBA-challenge/assets/161902555/e7613e01-5e8b-40d5-931a-53263f9809c6)

3. Click on `Enable Content` button.
   
![image](https://github.com/thaychansy/VBA-challenge/assets/161902555/a8286e70-2a0f-4701-be5c-f98e4460c1d2)

4. A user form name Calculations will pop-up and click on Calculate to run the VBA code.
   
![image](https://github.com/thaychansy/VBA-challenge/assets/161902555/fb0832ef-602e-4246-883c-79304ed2f2ce)

5. The VBA code will populate the Quarterly Change, Percent Change, and Total Stock Volume for each Quarter. As well as the Greatest % Increase, % Decrease and Greatest Total Volume of all of the Ticker names per Quarter.
   
Q1 Worksheet:

<img width="704" alt="image" src="https://github.com/thaychansy/VBA-challenge/assets/161902555/601d04b7-be60-45b9-8cdf-5444cda93fe6">


Q2 Worksheet:

<img width="673" alt="image" src="https://github.com/thaychansy/VBA-challenge/assets/161902555/7d3ef533-8119-4e8c-8855-8b3d27d1b382">


Q3 Worksheet:

<img width="676" alt="image" src="https://github.com/thaychansy/VBA-challenge/assets/161902555/1085814a-6cab-49ee-ab3b-760b57ce2412">

Q4 Worksheet:

<img width="681" alt="image" src="https://github.com/thaychansy/VBA-challenge/assets/161902555/9fc464a8-6def-4acc-a7a5-cb0cfb21fffd">




  

<p  align="right">(<a  href="#readme-top">back to top</a>)</p>

  
  

<!-- CONTRIBUTING -->

## Contributing 

(UC Berkeley Bootcamp Students Only)  

Contributions are what make the open source community such an amazing place to learn, inspire, and create. Any contributions you make are **greatly appreciated**.

  

If you have a suggestion that would make this better, please fork the repo and create a pull request. You can also simply open an issue with the tag "enhancement".

Don't forget to give the project a star! Thanks again!

  

1. Fork the Project

2. Create your Feature Branch (`git checkout -b new-branch-name`)

3. Commit your Changes (`git commit -m 'Add some message'`)

4. Push to the Branch (`git push origin new-branch-name`)

5. Create a pull request. 


Forking a repository and creating a pull request on GitHub is a great way to contribute to open-source projects. Here's a breakdown of the process:

1. Forking the Repository:

Find the repository you want to contribute to on GitHub.
Click on the "Fork" button in the top right corner. This creates a copy of the repository in your own account.

2. Clone the Forked Repository to Your Local Machine

You'll need Git installed on your system.
Use Git commands to clone your forked repository to your local machine. There will be instructions on the GitHub repository page for cloning.

3. Making Changes (Local Work):

Make your changes to the code in your local copy.
Use Git commands to track your changes (adding, committing).

4. Pushing Changes to Your Fork:

Once you're happy with your changes, use Git commands to push your local commits to your forked repository on GitHub.

5. Creating a Pull Request:

Go to your forked repository on GitHub.
Click the "Compare & pull request" button (might appear as a yellow banner).
Here, you'll see a comparison between your changes and the original repository.
Write a clear title and description for your pull request explaining the changes you made.
Click "Create Pull Request" to submit it for review.

<p  align="right">(<a  href="#readme-top">back to top</a>)</p>

  
  
  

<!-- LICENSE -->

## License

  

Distributed under the MIT License. See `LICENSE.txt` for more information.

  

<p  align="right">(<a  href="#readme-top">back to top</a>)</p>

  
  
  

<!-- CONTACT -->

## Contact

  

Thay Chansy - [@thaychansy](https://twitter.com/thaychansy) - or thay.chansy@gmail.com

Gursimran Kaur - kaursimran081999@gamil.com

Project Link: [thaychansy/VBA-challenge: Module 2 Challenge (github.com)](https://github.com/thaychansy/VBA-challenge)
  

<p  align="right">(<a  href="#readme-top">back to top</a>)</p>

  
  
  

<!-- ACKNOWLEDGMENTS -->

## Acknowledgments

  

Here's a list resources we found helpful and would like to give credit to. 

  
* [Chat GPT] [ChatGPT](https://chatgpt.com/)
* [Google Gemini] [Gemini Generative AI](https://gemini.google.com/app)
* [Stack Overflow] [ Stock Ticker Loop - Stack Overflow](https://stackoverflow.com/questions/48828163/stock-ticker-loop)
* [Stack Overflow] [VBA loop of multiple sheets in a worksheet - Stack Overflow](https://stackoverflow.com/questions/52012092/vba-loop-of-multiple-sheets-in-a-worksheet/52012335#52012335)
* [Stack Overflow] [How to apply a VBA code to every page in a workbook? - Stack Overflow](https://stackoverflow.com/questions/52122844/how-to-apply-a-vba-code-to-every-page-in-a-workbook-mine-does-part-of-the-code)


Collaboration and Contributions:

Special Thanks to Bootcamp Collaborator:
Gursimran Kaur (Simran) - kaursimran081999@gmail.com

  

<p  align="right">(<a  href="#readme-top">back to top</a>)</p>

  
  
  

<!-- MARKDOWN LINKS & IMAGES -->

<!-- https://www.markdownguide.org/basic-syntax/#reference-style-links -->

[contributors-shield]: https://img.shields.io/github/contributors/othneildrew/Best-README-Template.svg?style=for-the-badge

[contributors-url]: https://github.com/othneildrew/Best-README-Template/graphs/contributors

[forks-shield]: https://img.shields.io/github/forks/othneildrew/Best-README-Template.svg?style=for-the-badge

[forks-url]: https://github.com/othneildrew/Best-README-Template/network/members
