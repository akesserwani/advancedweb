import React, { useState } from 'react';

function App() {
  // Variable to deal with form inputs
  const [input, setInput] = useState('');
  // Variable to get todos
  const [todos, setTodos] = useState([]);

  // Handle form submission
  const handleSubmit = (e) => {
    e.preventDefault();
    if (input.trim() !== '') {
      setTodos([...todos, { text: input, isEditing: false }]);
      setInput('');
    }
  };

  // Handle input change
  const handleInputChange = (e) => {
    setInput(e.target.value);
  };

  // Handle delete todo
  const handleDelete = (index) => {
    const newTodos = todos.filter((todo, i) => i !== index);
    setTodos(newTodos);
  };

  // Handle edit todo
  const handleEdit = (index) => {
    const newTodos = todos.map((todo, i) =>
      i === index ? { ...todo, isEditing: !todo.isEditing } : todo
    );
    setTodos(newTodos);
  };

  // Handle save edit
  const handleSave = (index, newText) => {
    const newTodos = todos.map((todo, i) =>
      i === index ? { ...todo, text: newText, isEditing: false } : todo
    );
    setTodos(newTodos);
  };

  return (
    <>
      <div style={{ margin: '20px' }}>
        <form onSubmit={handleSubmit} style={{ display: 'flex', flexDirection: 'row', gap: '10px' }}>
          <input
            style={{ width: '30%' }}
            type="text"
            placeholder="Enter to do..."
            value={input}
            onChange={handleInputChange}
          />
          <button className="waves-effect waves-light btn green lighten-1" type="submit">
            Add
          </button>
        </form>
      </div>

      {/* List of displayed items */}
      <div style={{ display: 'flex', flexDirection: 'column', gap: '10px', margin: '20px' }}>
        {todos.map((todo, index) => (
          <div
            key={index}
            style={{
              width: '30%',
              height: 'auto',
              padding: '5px',
              display: 'flex',
              flexDirection: 'row',
              justifyContent: 'space-between',
            }}
          >
            {/* Item text */}
            {todo.isEditing ? (
              <input
                type="text"
                value={todo.text}
                onChange={(e) => {
                  const newTodos = [...todos];
                  newTodos[index].text = e.target.value;
                  setTodos(newTodos);
                }}
              />
            ) : (
              <h6 style={{ marginLeft: '5px' }}>{todo.text}</h6>
            )}
            {/* Item box with edit and delete */}
            <div style={{ width: '30%', display: 'flex', flexDirection: 'row', justifyContent: 'space-between' }}>
              {/* Edit/Save Icon */}
              <button
                className={`waves-effect waves-light btn ${todo.isEditing ? 'green' : 'blue'} lighten-1`}
                onClick={() => {
                  if (todo.isEditing) {
                    handleSave(index, todo.text);
                  } else {
                    handleEdit(index);
                  }
                }}
              >
                <i className="material-icons">{todo.isEditing ? 'save' : 'edit'}</i>
              </button>
              {/* Delete Icon */}
              <button className="waves-effect waves-light btn red lighten-2" onClick={() => handleDelete(index)}>
                <i className="material-icons">delete</i>
              </button>
            </div>
          </div>
        ))}
      </div>
    </>
  );
}

export default App;
