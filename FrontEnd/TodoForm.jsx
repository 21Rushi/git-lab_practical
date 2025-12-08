import { useState } from "react";

export default function TodoForm() {
  const [itemName, setItemName] = useState("");
  const [itemDescription, setItemDescription] = useState("");

  const handleSubmit = (e) => {
    e.preventDefault();
    console.log(itemName, itemDescription);
  };

  return (
    <form onSubmit={handleSubmit}>
      <input placeholder="Item Name" onChange={(e) => setItemName(e.target.value)} />
      <textarea placeholder="Item Description" onChange={(e) => setItemDescription(e.target.value)} />
      <button type="submit">Submit</button>
    </form>
  );
}

