<!DOCTYPE html>
<html lang="en">

<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Math Quest</title>
    <style>
        html, body {
            margin: 0;
            padding: 0;
            background-color: black;
            color: white;
            height: 100%;
            overflow: hidden;
        }

        canvas {
            display: block;
            margin: auto;
            width: 100vw;
            height: 100vh;
            touch-action: manipulation;
        }

        #loading,
        #error,
        #general-errors {
            position: absolute;
            top: 50%;
            left: 50%;
            transform: translate(-50%, -50%);
            color: white;
            font-family: sans-serif;
            text-align: center;
        }

        #loading span,
        #error span,
        #general-errors span {
            display: block;
            font-size: 1.5rem;
            margin-top: 10px;
        }

        #general-errors {
            font-size: 1rem;
            color: yellow;
        }
    </style>
</head>

<body>
    <!-- Loading Message -->
    <div id="loading">
        <img src="logo.png" alt="Math Quest Logo" width="200" />
        <span>🔄 Loading game...</span>
    </div>

    <!-- Error Message -->
    <div id="error" style="display: none;">
        <span>❌ Game engine failed to load!</span>
    </div>

    <!-- General Errors -->
    <div id="general-errors" style="display: none;">
        <span>⚠️ Some errors occurred!</span>
    </div>

    <!-- Importing Pygbag -->
    <script src="https://cdn.jsdelivr.net/npm/pygbag@0.1.0/pygbag.js"></script>

    <!-- Your Game Script -->
    <script src="js/main.js"></script>

</body>

</html>
