# PyQt5 Todo Application

A simple, elegant to-do list application built with PyQt5, implementing the Model-View-Controller (MVC) architecture pattern.

![Todo App Screenshot](screenshots/todo_app.png)

## Features

- Add and delete tasks
- Persistent storage - tasks are saved to a text file and loaded when the application starts
- Clean, minimalist user interface
- MVC architecture for better code organization and maintainability

## Project Structure

```
todo/
├── app/
│   ├── controller/
│   │   └── todoController.py
│   ├── model/
│   │   └── todoModel.py
│   └── view/
│       └── todoView.py
├── data/
│   └── tasks.txt
├── widgets/
│   ├── todo_button.py
│   ├── todo_lineedit.py
│   └── todo_list.py
├── main.py
└── README.md
```

## Architecture

This application follows the Model-View-Controller (MVC) pattern:

- **Model** (`todoModel.py`): Handles data storage and retrieval operations (loading and saving tasks)
- **View** (`todoView.py`): Defines the user interface and display components
- **Controller** (`todoController.py`): Manages the application logic and user interactions

## Components

### Custom Widgets

- `TodoLineedit`: A customized QLineEdit component for task input
- `TodoButton`: A customized QPushButton component for action buttons
- `TodoList`: A customized QListWidget component for displaying tasks

### Core Classes

- `TodoModel`: Handles file operations for saving and loading tasks
- `TodoView`: Manages the visual representation of the application
- `TodoController`: Connects user actions to data operations

## Installation

### Prerequisites

- Python 3.6 or higher
- PyQt5

### Setup

1. Clone the repository:
   ```
   git clone https://github.com/yourusername/todo-pyqt.git
   cd todo-pyqt
   ```

2. Install the required packages:
   ```
   pip install PyQt5
   ```

3. Run the application:
   ```
   python main.py
   ```

## Usage

1. Enter a task in the text field
2. Click "Task hinzufügen" to add the task to the list
3. Select a task and click "Task löschen" to remove it
4. Tasks are automatically saved when you close the application

## Development

### Extending the Application

To add new features:

1. Update the model if new data operations are needed
2. Add UI elements to the view
3. Connect the new UI elements to controller methods
4. Implement the logic in the controller

### Custom Styling

The application uses PyQt5's styling capabilities. You can modify the appearance by:

1. Creating CSS-like stylesheets
2. Setting them using `setStyleSheet()` method on widgets
3. Customizing widget properties in their respective classes

## Contributing

1. Fork the project
2. Create your feature branch (`git checkout -b feature/amazing-feature`)
3. Commit your changes (`git commit -m 'Add some amazing feature'`)
4. Push to the branch (`git push origin feature/amazing-feature`)
5. Open a Pull Request

## License

This project is licensed under the MIT License - see the LICENSE file for details.

## Acknowledgments

- PyQt5 documentation and community
- MVC architecture pattern resources
