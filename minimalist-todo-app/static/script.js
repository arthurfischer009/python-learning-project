// Game state
let startTime = Date.now();
let timerInterval = null;
let currentState = null;

// DOM elements
const gameActiveScreen = document.getElementById('game-active-screen');
const gameOverScreen = document.getElementById('game-over-screen');
const currentTaskEl = document.getElementById('current-task');
const levelBadge = document.getElementById('level-badge');
const skipsBadge = document.getElementById('skips-badge');
const timerEl = document.getElementById('timer');
const timerWarning = document.getElementById('timer-warning');
const progressFill = document.getElementById('progress-fill');
const progressText = document.getElementById('progress-text');
const completeBtn = document.getElementById('complete-btn');
const skipBtn = document.getElementById('skip-btn');
const quitBtn = document.getElementById('quit-btn');
const resetBtn = document.getElementById('reset-btn');

// Timer functionality
function startTimer() {
    startTime = Date.now();

    if (timerInterval) {
        clearInterval(timerInterval);
    }

    timerInterval = setInterval(() => {
        const elapsed = Math.floor((Date.now() - startTime) / 1000);
        const minutes = Math.floor(elapsed / 60);
        const seconds = elapsed % 60;

        timerEl.textContent = `${String(minutes).padStart(2, '0')}:${String(seconds).padStart(2, '0')}`;

        // Show warning at 50 minutes
        if (minutes >= 50) {
            timerWarning.classList.remove('hidden');
            timerEl.classList.add('timer-warning-active');
        }

        // Flash at 60 minutes
        if (minutes >= 60) {
            timerEl.classList.add('timer-danger');
        }
    }, 1000);
}

function stopTimer() {
    if (timerInterval) {
        clearInterval(timerInterval);
        timerInterval = null;
    }
}

// Fetch and update game state
async function updateGameState() {
    try {
        const response = await fetch('/api/game-state');
        const data = await response.json();

        if (data.game_over) {
            showGameOver(data);
            return;
        }

        currentState = data;

        // Update UI
        currentTaskEl.textContent = data.current_task;
        levelBadge.textContent = `Level ${data.level}`;

        // Update skips badge
        const skipsRemaining = data.skips_remaining;
        skipsBadge.textContent = `${skipsRemaining} skip${skipsRemaining !== 1 ? 's' : ''} left`;
        skipBtn.disabled = skipsRemaining === 0;

        // Update progress
        const progress = (data.level / data.total_levels) * 100;
        progressFill.style.width = `${progress}%`;
        progressText.textContent = `${data.level} / ${data.total_levels}`;

        // Reset timer for new task
        startTimer();

        // Add entrance animation
        currentTaskEl.classList.add('task-appear');
        setTimeout(() => currentTaskEl.classList.remove('task-appear'), 500);

    } catch (error) {
        console.error('Error fetching game state:', error);
    }
}

function showGameOver(data) {
    stopTimer();
    gameActiveScreen.classList.add('hidden');
    gameOverScreen.classList.remove('hidden');

    document.getElementById('completed-count').textContent = data.completed;
    document.getElementById('skipped-count').textContent = data.skipped;

    // Celebration animation
    gameOverScreen.classList.add('celebration-animation');
}

// Complete current task
async function completeTask() {
    completeBtn.disabled = true;
    completeBtn.textContent = 'Level Up! 🎉';

    try {
        const response = await fetch('/api/complete', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json',
            }
        });

        if (response.ok) {
            // Add celebration effect
            currentTaskEl.classList.add('task-complete');

            setTimeout(() => {
                updateGameState();
                completeBtn.disabled = false;
                completeBtn.textContent = 'Complete ✓';
            }, 800);
        }
    } catch (error) {
        console.error('Error completing task:', error);
        completeBtn.disabled = false;
        completeBtn.textContent = 'Complete ✓';
    }
}

// Skip current task
async function skipTask() {
    if (!confirm('Skip this level? You can only skip 2 levels total.')) {
        return;
    }

    skipBtn.disabled = true;

    try {
        const response = await fetch('/api/skip', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json',
            }
        });

        if (response.ok) {
            currentTaskEl.classList.add('task-skip');

            setTimeout(() => {
                updateGameState();
                skipBtn.disabled = false;
            }, 600);
        } else {
            const data = await response.json();
            alert(data.error || 'Cannot skip task');
            skipBtn.disabled = false;
        }
    } catch (error) {
        console.error('Error skipping task:', error);
        skipBtn.disabled = false;
    }
}

// Reset game
async function resetGame() {
    if (!confirm('Are you sure you want to reset the game? All progress will be lost.')) {
        return;
    }

    try {
        const response = await fetch('/api/reset', {
            method: 'POST',
        });

        if (response.ok) {
            stopTimer();
            window.location.href = '/';
        }
    } catch (error) {
        console.error('Error resetting game:', error);
    }
}

// Event listeners
completeBtn.addEventListener('click', completeTask);
skipBtn.addEventListener('click', skipTask);
quitBtn.addEventListener('click', resetGame);
resetBtn.addEventListener('click', resetGame);

// Keyboard shortcuts
document.addEventListener('keydown', (e) => {
    if (e.key === 'Enter' && !completeBtn.disabled) {
        completeTask();
    }
});

// Initialize game
updateGameState();
