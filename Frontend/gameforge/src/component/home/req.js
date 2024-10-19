function Lister({ game }) {
    return <button className="template-button">{game}</button>;
}

export default function List(){
    const Games = [
        "Tic-Tac-Toe",
        "Hangman",
        "Rock, Paper, Scissors",
        "Snake Game",
        "Text Adventure Game",
        "Minesweeper (text-based)",
        "Number Guessing Game",
        "Chess",
        "Connect Four",
        "Mastermind",
        "Checkers",
        "2048",
        "Word Scramble",
        "Battleship",
        "Sudoku Solver/Player",
        "Quiz Game",
        "Dungeon Crawler",
        "Nim",
        "Blackjack",
        "Memory Game",
        "Snake and Ladder"
    ];
    return (
        <div className="home-options">
                <div className="custom">
                    <form className="forms">
                        <label>Project Brief</label>
                        <textarea className="task" rows="10" placeholder="Describe your project..." />
                        <label>Preferred Programming Languages</label>
                        <input type="text" className="lang" placeholder="Enter languages..." />
                        <input type="submit" className="submit-button" value="Generate" />
                    </form>
                </div>

                <div className="templates" >
                    <h2>Premade Templates</h2>
                    <div className="template-buttons">
                        {Games.map((game, index) => (
                            <Lister key={index} game={game} />
                        ))}
                    </div>
                </div>
        </div>
    );
};