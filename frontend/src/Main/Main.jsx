import React, { useEffect, useState } from "react";
import {
  useNavigate
} from "react-router-dom";
import Button from '@mui/material/Button';
import Typography from '@mui/material/Typography';
import TextField from '@mui/material/TextField';
import Accordion from '@mui/material/Accordion';
import AccordionSummary from '@mui/material/AccordionSummary';
import AccordionDetails from '@mui/material/AccordionDetails';
import KeyboardBackspaceIcon from '@mui/icons-material/KeyboardBackspace';
import ExpandMoreIcon from '@mui/icons-material/ExpandMore';
import IconButton from '@mui/material/IconButton';
import Header from "../Header/Header";
import '../App.css';

function Main() {

  const navigate = useNavigate();
  const [topics, setTopics] = useState([])
  const [task, setTask] = useState()
  const [email, setEmail] = useState("")

  const getTopics = () => {
    fetch("/api/topics/", {
      method: "GET",
      headers: new Headers({
        'Authorization': `Token ${sessionStorage.getItem('auth_token')}`,
      }),
    })
      .then((response) => {
        response.json().then(value => {
          setTopics(value)
        })
      })
  }

  const getTask = (id) => {
    fetch(`/api/tasks/${id}/`, {
      method: "GET",
      headers: new Headers({
        'Authorization': `Token ${sessionStorage.getItem('auth_token')}`,
      }),
    })
      .then((response) => {
        response.json().then(value => {
          setTask(value)
        })
      })
  }

  const checkUrl = () => {
    fetch(`/api/solution-testing/`, {
      method: "POST",
      headers: new Headers({
        'Content-Type': 'application/json',
        'Authorization': `Token ${sessionStorage.getItem('auth_token')}`,
      }),
      body: JSON.stringify({
        github_url: email
      })
    })
      .then((response) => {
        response.json().then(value => {
          checkUrl2(value.id)
        })
      })
  }

  const checkUrl2 = (id) => {
    let timerId = setInterval(() => {
      fetch(`/api/solution-testing/${id}/`, {
        method: "GET",
        headers: new Headers({
          'Authorization': `Token ${sessionStorage.getItem('auth_token')}`,
        })
      })
        .then((response) => {
          response.json().then(value => {
            if (value.status === "SUCCESS") {
              clearInterval(timerId);
              getSolutions(value.id)
            }
          })
        })
    }, 5000);
  }

  const getSolutions = (id) => {
    fetch(`/api/solutions/${id}/`, {
      method: "GET",
      headers: new Headers({
        'Authorization': `Token ${sessionStorage.getItem('auth_token')}`,
      })
    })
      .then((response) => {
        response.json().then(value => {
          navigate("/solution", {
            state: value
          })
        })
      })
  }

  useEffect(getTopics, [])

  return (
    <React.Fragment>
      <div className="header">
        {sessionStorage.getItem('username')}
        <Button variant="contained" onClick={() => {
          sessionStorage.setItem('auth_token', "");
          navigate("/")
        }}>Выйти</Button>
      </div>
      <div className="main">
        <div className="twoContent">
          {
            task
              ? (
                <div className="main">
                  <div className="title">
                    <IconButton color="primary" onClick={() => setTask()}>
                      <KeyboardBackspaceIcon />
                    </IconButton>
                    <h4>{task.name}</h4>
                  </div>
                  {task.description}
                </div>
              )
              : (
                <div className="main">
                  <h3>Список модулей</h3>
                  {topics.map(topic => (
                    <Accordion>
                      <AccordionSummary
                        expandIcon={<ExpandMoreIcon />}
                        aria-controls="panel1a-content"
                        id="panel1a-header"
                      >
                        <Typography>{topic.name}</Typography>
                      </AccordionSummary>
                      {topic.tasks.map(task => (
                        <AccordionDetails>
                          <Typography onClick={() => {
                            getTask(task.id)
                          }}>
                            {task.name}
                          </Typography>
                        </AccordionDetails>
                      ))}
                    </Accordion>
                  ))}
                </div>
              )
          }
          <div className="main">
            <h3>Проверить репозиторий</h3>
            <TextField
              id="outlined-required"
              label="Email"
              value={email}
              onChange={(e) => setEmail(e.target.value)}
              fullWidth
              margin="normal"
            />
            <Button variant="contained" onClick={checkUrl}>Проверить</Button>
          </div>
        </div>
      </div>
    </React.Fragment>
  );
}

export default Main;
