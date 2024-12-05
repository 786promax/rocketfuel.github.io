<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <script src="https://cdn.tailwindcss.com"></script>
    <script>
        tailwind.config = {
            darkMode: 'selector',
            theme: {
                extend: {
                colors: {
                    clifford: '#da373d',
          }
        }
      }
    }
    </script>
</head>
<body class="bg-white dark:bg-slate-800 transition-colors">
    <nav class="flex justify-between bg-gradient-to-r from-indigo-500 from 10% via-sky-500 via-30% to-emerald-500">
        <span class="px-20 py-4 font-semibold text-xl text-white transform-gpu transition-transform hover:-translate-y-1">Aatif's Website</span>
        <ul class="px-28 text-[17px] py-4 flex space-x-6 justify-end font-mono">
            <a href="htme.jpg"><li class="border-2 border-slate-200 hover:border-2 hover:border-slate-800 transform-gpu transition-transform text-white hover:bg-orange-500 hover:-translate-y-1 px-4 rounded-full py-[5px]">Home</li></a>
            <a href="htme.jpg"><li class="border-2 border-slate-200 hover:border-2 hover:border-slate-800 transform-gpu transition-transform text-white hover:bg-orange-500 hover:-translate-y-1 px-4 rounded-full py-[5px]">Projects</li></a>
                    <a href="htme.jpg"><li class="border-2 border-slate-200 hover:border-2 hover:border-slate-800 transform-gpu transition-transform text-white hover:bg-orange-500 hover:-translate-y-1 px-4 rounded-full py-[5px]">Join Us</li></a>
            <button onclick="darkmode()" id = "darkmode-btn" class="transform-gpu transition-transform hover:-translate-y-1"><img class = "w-8" src="dark.svg"></button>
        </ul>
    </nav>
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Test 1205</title>
    <style>
        body {font-family: Arial, Helvetica, sans-serif;}
        input[type=text], input[type=password] {
            width: 100%;
            padding: 12px 20px;
            margin: 8px 0;
            display: inline-block;
            border: 1px solid #ccc;
            box-sizing: border-box;
        }
        button {
            background-color: #04AA6D;
            color: white;
            padding: 14px 20px;
            margin: 8px 0;
            border: none;
            cursor: pointer;
            width: 100%;
        }
        button:hover {opacity: 0.8;}
        .cancelbtn {
            width: auto;
            padding: 10px 18px;
            background-color: #f44336;
        }
        .modal {
            display: none;
            position: fixed;
            z-index: 1;
            left: 0;
            top: 0;
            width: 100%;
            height: 100%;
            overflow: auto;
            background-color: rgba(0,0,0,0.4);
            padding-top: 60px;
        }
        .modal-content {
            background-color: #fefefe;
            margin: 5% auto;
            border: 1px solid #888;
            width: 80%;
            padding: 20px;
        }
        .imgcontainer {
            text-align: center;
            margin: 24px 0 12px 0;
        }
        img.avatar {
            width: 40%;
            border-radius: 50%;
        }
        .close {
            position: absolute;
            right: 25px;
            top: 0;
            color: #000;
            font-size: 35px;
            font-weight: bold;
        }
        .close:hover, .close:focus {
            color: red;
            cursor: pointer;
        }
    </style>
</head>
<body>
<h9>Made by me/me </h9>
<h2>Enter your passord here hehe</h2>
<button onclick="document.getElementById('id01').style.display='block'" style="width:auto;">Login</button>

<div id="id01" class="modal">
    <div class="modal-content">
        <div class="imgcontainer">
            <span onclick="document.getElementById('id01').style.display='none'" class="close" title="Close Modal">&times;</span>
            <img src="img_avatar2.png" alt="Avatar" class="avatar">
        </div>
        <form id="loginForm" onsubmit="return redirectToSite(event)">
            <div class="container">
                <label for="uname"><b>Username</b></label>
                <input type="text" id="uname" placeholder="Enter Username" required>

                <label for="psw"><b>Password</b></label>
                <input type="password" id="psw" placeholder="Enter Password" required>

                <button type="submit">Login</button>
                <label>
                    <input type="checkbox" checked="checked" name="remember"> Remember me
                </label>
            </div>
            <div class="container" style="background-color:#f1f1f1">
                <button type="button" onclick="document.getElementById('id01').style.display='none'" class="cancelbtn">Cancel</button>
                <span class="psw">Forgot <a href="#">password?</a></span>
            </div>
        </form>
    </div>
</div>

<script>
// Close modal when clicking outside of it
window.onclick = function(event) {
    const modal = document.getElementById('id01');
    if (event.target == modal) {
        modal.style.display = "none";
    }
};

// Redirect without validation
function redirectToSite(event) {
    event.preventDefault(); // Prevent default form submission
    alert("Redirecting to the site...");
    window.location.href = "https://786promax.github.io/voie.github.io/"; // Replace with your desired URL
}
</script>

</body>
</html>
