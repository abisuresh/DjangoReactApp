import React from 'react';
import ReactDOM from "react-dom";
import RecipeCreation from "./App";

ReactDOM.render(
  // Our main React application component, which we've imported from another file
  <RecipeCreation />,
  // Gets rendered to the <div> we defined in our Django template using the shared id
  document.getElementById('js-framework-home')
);