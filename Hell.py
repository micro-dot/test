<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <link href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.0.0-beta3/css/all.min.css" rel="stylesheet">
    <title>Maskbook Feed</title>
    <style>
        /* Global Styles */
        body {
            margin: 0;
            padding: 0;
            background-color: #000;
            color: #fff;
            font-family: 'Arial', sans-serif;
            overflow: hidden;
        }

        /* Header Section */
        .header {
            text-align: left;
            padding: 20px;
            font-size: 22px;
            color: #4a90e2;
            font-weight: bold;
            position: fixed;
            top: 0;
            left: 0;
            right: 0;
            z-index: 100;
            background-color: #121212;
            box-sizing: border-box;
        }
        
 .draggable {
            font-size: 40px;
            color: #4a90e2;
            cursor: grab;
            position: fixed;
            top: 50%; /* Center vertically */
            left: 85%; /* Center horizontally */
            transform: translate(-50%, -50%);
        }



        /* Icons Navigation */
        .icons {
            display: flex;
            justify-content: space-evenly;
            padding-bottom: 20px;
            position: fixed;
            top: 60px;
            left: 0;
            right: 0;
            z-index: 100;
            background-color: #121212;
            border-bottom: 1px solid #222;
        }

        .icon {
            width: 50px;
            height: 50px;
            display: flex;
            justify-content: center;
            align-items: center;
            background-color: #333;
            border-radius: 50%;
            color: #4a90e2;
            font-size: 20px;
            transition: background-color 0.3s, transform 0.3s;
        }

        .icon:hover {
            background-color: #4a90e2;
            color: #fff;
            transform: translateY(-5px);
        }

        /* Feed Section */
        .feed-scroll {
            position: fixed;
            top: 120px;
            left: 0;
            right: 0;
            bottom: 70px;
            overflow-y: scroll;
            scroll-snap-type: y mandatory;
            scrollbar-width: none; /* Hide scrollbar */
        }

        .feed-scroll::-webkit-scrollbar {
            display: none;
        }

        .feed-container {
            height: 100%; /* Full screen height for perfect centering */
            scroll-snap-align: center; /* Ensures alignment in the center when scrolling */
            display: flex;
            flex-direction: column;
            justify-content: center;
            align-items: center;
            padding: 20px;
            background-color: #121212;
        }

        /* Post Header */
        .feed-header {
            display: flex;
            align-items: center;
            margin-bottom: 20px;
            gap: 10px;
        }

        .profile {
            display: flex;
            align-items: center;
            justify-content: center;
            font-size: 34px;
            border-radius: 50%;
            border: 2px solid #4a90e2;
            width: 50px;
            height: 50px;
        }

        .text-container {
            display: flex;
            flex-direction: column;
            justify-content: center;
        }

        .text-container span {
            font-size: 16px;
            color: #aaa;
        }

        .text-container .username {
            font-size: 18px;
            font-weight: bold;
            color: #fff;
        }

        /* Post Content */
        .post-container {
            width: 90%;
            max-width: 500px;
            background-color: #1e1e1e;
            border-radius: 15px;
            color: #ddd;
            text-align: left;
            padding: 20px;
            word-wrap: break-word;
            overflow: hidden;
            display: flex;
            flex-direction: column;
            justify-content: center;
        }

        .hashtags {
            color: #9c27b0;
            font-style: italic;
            margin-top: 10px;
        }

        .actions {
            display: flex;
            justify-content: space-between;
            align-items: center;
            margin-top: 20px;
            gap: 10px;
        }

        .actions span {
            display: flex;
            align-items: center;
            gap: 5px;
            cursor: none;
            transition: transform 0.3s, color 0.3s;
            padding: 10px 25px;
            border-radius: 10px;
        }

        .actions .like {
            color: #e53935;
            background-color: #333;
            border: 1px solid #e53935;
        }

        .actions .like:hover {
            background-color: #e57373;
            color: #fff;
        }

        .actions .comment {
            color: #43a047;
            background-color: #333;
            border: 1px solid #43a047;
        }

        .actions .comment:hover {
            background-color: #66bb6a;
            color: #fff;
        }

        /* Footer Navigation */
        .nav-buttons {
            display: flex;
            justify-content: space-evenly;
            padding: 15px;
            background-color: #121212;
            border-top: 1px solid #222;
            position: fixed;
            bottom: 0;
            left: 0;
            right: 0;
            z-index: 99;
        }

        .nav-button {
            width: 55px;
            height: 55px;
            display: flex;
            justify-content: center;
            align-items: center;
            font-size: 24px;
            color: #4a90e2;
            background-color: #222;
            border: 1px solid #4a90e2;
            border-radius: 50%;
            transition: background-color 0.3s, color 0.3s;
        }

        .nav-button:hover {
            background-color: #4a90e2;
            color: #fff;
        }
        
        /* Spinner Styles */
        .spinner {
            position: fixed;
            top: 50%;
            left: 50%;
            transform: translate(-50%, -50%);
            display: none;
            width: 50px;
            height: 50px;
            border: 5px solid #4a90e2;
            border-top: 5px solid transparent;
            border-radius: 50%;
            animation: spin 1s linear infinite;
        }

        @keyframes spin {
            0% {
                transform: translate(-50%, -50%) rotate(0deg);
            }
            100% {
                transform: translate(-50%, -50%) rotate(360deg);
            }
        }
        #search{
          font-size: 15px;
          display: flex;
          position: fixed;
          left: 85%;
          top: 3%;
          padding: 2%;
          border-radius: 50%;
          background-color:#333;
          transition: background-color 0.3s, transform 0.3s;
        }
        #search:hover{
          background-color: #4a90e2;
            color: #fff;
            transform: translateY(-5px);
        }
    </style>
</head>
<body>
    <div class="header">maskbook<i id="search" onclick="location.href='/search'" class="fa-solid fa-magnifying-glass"></i></div>
    <div class="icons">
        <button class="icon" onclick="location.href='/market'"><i class="fa-solid fa-shop"></i></button>
        <button class="icon" onclick="location.href='/frienders'" >💬</button>
        <button class="icon" onclick="location.href='/notify'">🔔</button>
    </div>
    <div class="feed-scroll" id="feed-scroll">
        {% for post in posts %}
        <div class="feed-container">
            <div class="feed-header">
                <div class="profile">{{post.profile_picture}}</div>
                <div class="text-container">
                    <span class="username">{{post.first_name}} {{post.last_name}}</span>
                    <span>• @{{post.username}}</span>
                </div>
            </div>
            <div class="post-container">
                <p>{{post.content}}</p>
                <div class="hashtags">{{post.tag}}</div>
            </div>
            <div class="actions">
                <span class="like" id="like-{{ post.id }}" onclick="toggleLike({{ post.id }})">♥️ {{ post.formatted_like_count }}</span>
                <span class="comment" onclick="location.href='/comments/{{post.id}}'">💬 {{ post.formatted_comment_count }}</span>
            </div>
             <i id="robot" class="fas fa-robot draggable" onclick="location.href='/myai'"></i>
        </div>
        {% endfor %}
    </div>
    <div class="nav-buttons">
        <button class="nav-button" id="home-button">🏠</button>
        <button class="nav-button" onclick="location.href='/post'">📷</button>
        <button class="nav-button" onclick="location.href='/profile'">👤</button>
    </div>
    <div class="spinner" id="spinner"></div>
    <script>
const robot = document.getElementById("robot");

        let isDragging = false;
        let offsetX = 0, offsetY = 0;

        // Mouse down: Start dragging
        robot.addEventListener("mousedown", (e) => {
            isDragging = true;
            offsetX = e.clientX - robot.getBoundingClientRect().left;
            offsetY = e.clientY - robot.getBoundingClientRect().top;
            robot.style.cursor = "grabbing";
        });

        // Mouse move: Drag the icon
        document.addEventListener("mousemove", (e) => {
            if (!isDragging) return;
            const x = e.clientX - offsetX;
            const y = e.clientY - offsetY;
            robot.style.left = `${x}px`;
            robot.style.top = `${y}px`;
        });

        // Mouse up: Stop dragging
        document.addEventListener("mouseup", () => {
            isDragging = false;
            robot.style.cursor = "grab";
        });

        // Optional: Touch support for mobile devices
        robot.addEventListener("touchstart", (e) => {
            isDragging = true;
            const touch = e.touches[0];
            offsetX = touch.clientX - robot.getBoundingClientRect().left;
            offsetY = touch.clientY - robot.getBoundingClientRect().top;
            robot.style.cursor = "grabbing";
        });

        document.addEventListener("touchmove", (e) => {
            if (!isDragging) return;
            const touch = e.touches[0];
            const x = touch.clientX - offsetX;
            const y = touch.clientY - offsetY;
            robot.style.left = `${x}px`;
            robot.style.top = `${y}px`;
        });

        document.addEventListener("touchend", () => {
            isDragging = false;
            robot.style.cursor = "grab";
        });

const homeButton = document.getElementById('home-button');
const spinner = document.getElementById('spinner');

if (homeButton) {
    homeButton.addEventListener('click', () => {
        showSpinner();
        refreshFeed();
    });
}

function showSpinner() {
    if (spinner) {
        spinner.style.display = 'block'; // Show the spinner
    }
}

function hideSpinner() {
    if (spinner) {
        spinner.style.display = 'none'; // Hide the spinner
    }
}

function refreshFeed() {
    // Simulate an action (e.g., fetching data)
    setTimeout(() => {
        window.location.reload(); // Reload the page
    }, 1000); // Adjust delay as needed for your application
}
    function toggleLike(postId) {
    const likeButton = document.querySelector(`#like-${postId}`);
    
    fetch(`/like_comment/${postId}`, { method: 'GET' })
        .then(response => {
            if (!response.ok) {
                throw new Error('Network response was not ok');
            }
            return response.json();
        })
        .then(data => {
            if (data.errorMessage) {
                console.error('Error:', data.errorMessage);
                likeButton.innerHTML = `<span style="color: red;">Error!</span>`;
                return;
            }

            // Update only the like count while keeping the heart emoji intact
            const heartEmoji = likeButton.innerHTML.split(' ')[0]; // Get the heart emoji (either filled or empty)
            likeButton.innerHTML = `${heartEmoji} ${data.formatted_like_count}`;
        })
        .catch(error => {
            console.error('Error:', error);
            likeButton.innerHTML = `<span style="color: red;">Error!</span>`;
        });
}
</script>
</body>
</html>

