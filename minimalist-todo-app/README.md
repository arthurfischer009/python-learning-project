# Level Up - Minimalist Todo App

A beautiful, minimalist todo app that gamifies your tasks. Focus on ONE task at a time, level up when you complete it!

## Features

- **One Task at a Time** - Stay focused on what matters
- **Level System** - Tasks are "levels" you complete
- **1 Hour Time Limit** - Each task should take max 1 hour
- **Skip Feature** - Can skip up to 2 tasks
- **Beautiful UI** - Clean, iOS-inspired minimalist design
- **Timer** - Track how long you spend on each level
- **Progress Tracking** - See your completion stats
- **Responsive** - Works great on mobile and desktop

## Installation

1. Navigate to the project directory:
```bash
cd minimalist-todo-app
```

2. Install dependencies:
```bash
pip install -r requirements.txt
```

## How to Run

1. Start the Flask server:
```bash
python app.py
```

2. Open your browser and go to:
```
http://localhost:5000
```

## How to Play

1. **Setup Phase** - Add your tasks (levels) before starting
   - Each task should take approximately 1 hour or less
   - Add as many tasks as you want

2. **Game Phase** - Focus on one level at a time
   - Complete the task and click "Complete" to level up
   - Skip a task if needed (max 2 skips)
   - Timer shows how long you've spent on the current level
   - Warning appears at 50 minutes

3. **Game Over** - See your stats
   - View completed vs skipped tasks
   - Start a new game

## Project Structure

```
minimalist-todo-app/
├── app.py              # Flask backend
├── tasks.json          # Game state (auto-generated)
├── requirements.txt    # Python dependencies
├── static/
│   ├── style.css      # Beautiful minimalist styling
│   └── script.js      # Game logic and interactions
└── templates/
    ├── index.html     # Setup screen
    └── game.html      # Game screen
```

## Features in Detail

### Timer
- Starts automatically for each task
- Shows warning at 50 minutes (yellow)
- Shows danger at 60 minutes (red, shaking)

### Skip System
- Maximum 2 skips per game
- Confirmation dialog before skipping
- Skip counter updates in real-time

### Progress Bar
- Visual progress through all levels
- Smooth animations

### Keyboard Shortcuts
- **Enter** - Complete current task

## Design Philosophy

This app follows a minimalist, iOS-inspired design:
- Clean white cards with subtle shadows
- Gradient background
- Smooth animations
- Focus on one task at a time
- Beautiful typography with Inter font
- Responsive design for all devices

## Technologies Used

- **Backend**: Python Flask
- **Frontend**: Vanilla JavaScript (no frameworks!)
- **Styling**: Pure CSS with beautiful animations
- **Storage**: JSON file
- **Font**: Google Fonts (Inter)

## Mobile Experience

The app is fully responsive and works great on mobile devices:
- Touch-optimized buttons
- Responsive layout
- iOS Safari optimizations
- Can be added to home screen as PWA-style app

## Future Enhancements

Potential features for future versions:
- Sound effects and haptic feedback
- Dark mode
- Daily streaks
- Task categories
- Time analytics
- Progressive Web App (full offline support)
- Achievements and rewards

## License

Free to use and modify!

---

**Enjoy leveling up your productivity!** 🎯
