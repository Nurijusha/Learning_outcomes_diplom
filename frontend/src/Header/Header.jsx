import React, { useState } from "react";
import Button from '@mui/material/Button';
import '../App.css';

function Header({ title, onClick }) {
  return (
    <div className="header">
      <Button variant="contained" onClick={onClick}>{title}</Button>
    </div>
  );
}

export default Header;
