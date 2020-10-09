instructions = [
    "SET FOREIGN_KEY_CHEKS = 0;",
    "DROP TABLE IF EXISTS user;",
    "DROP TABLE IF EXISTS blog;",
    "SET FOREIGN_KEY_CHEKS = 1;",
    """
        CREATE TABLE user (
            id INT PRIMARY KEY AUTO_INCREMENT,
            username VARCHAR(50) UNIQUE NOT NULL,
            password VARCHAR(100) NOT NULL
        )
    """,
    """
        CREATE TABLE blog (
            id INT PRIMARY KEY AUTO_INCREMENT,
            created_by INT NOT NULL,
            created_at TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP,
            title TEXT NOT NULL,
            blog TEXT NOT NULL,
            FOREIGN KEY (created_by) REFERENCES user (id)
        );
    """
]