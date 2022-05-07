import React from "react";
import Button from '@mui/material/Button';
import {
  useNavigate
} from "react-router-dom";
import '../App.css';

function Congratulation() {
  const navigate = useNavigate();

  return (
    <div className="contentCenter">
      <div className="authBlock">
        <h2>Завершение регистрации</h2>
        Поздравляем! Вы зарегистрировались!
        <Button variant="outlined" onClick={() => navigate("/")} >Войти</Button>
      </div>
    </div>
  );
}

export default Congratulation;
