import React, { useEffect, useMemo, useState } from "react";
import Button from '@mui/material/Button';
import {
  useNavigate,
  useLocation
} from "react-router-dom";
import '../App.css';

import Table from '@mui/material/Table';
import TableBody from '@mui/material/TableBody';
import TableCell from '@mui/material/TableCell';
import TableContainer from '@mui/material/TableContainer';
import TableHead from '@mui/material/TableHead';
import TableRow from '@mui/material/TableRow';
import Paper from '@mui/material/Paper';

import { Chart as ChartJS, ArcElement, Tooltip, Legend } from 'chart.js';
import { Pie } from 'react-chartjs-2';

ChartJS.register(ArcElement, Tooltip, Legend);

function Solution() {
  const navigate = useNavigate();
  const location = useLocation();
  const [score, setScore] = useState({
    5: 0,
    4: 0,
    3: 0,
    2: 0
  });

  useEffect(() => {
    const newscore = {
      5: 0,
      4: 0,
      3: 0,
      2: 0
    }
    location.state.learning_outcomes.map((value) => newscore[value.score] = newscore[value.score] + 1);
    setScore(newscore)
  }, [location])

  const data = useMemo(() => {
    return {
      labels: ['на 2', 'на 3', 'на 4', 'на 5'],
      datasets: [
        {
          label: '# of Votes',
          data: Object.values(score),
          backgroundColor: [
            'rgba(255, 99, 132, 0.2)',
            'rgba(54, 162, 235, 0.2)',
            'rgba(255, 206, 86, 0.2)',
            'rgba(75, 192, 192, 0.2)',
          ],
          borderWidth: 1,
        },
      ],
    };
  }, [score])

  return (
    <div className="contentCenter">
      <div className="solution">
        <h1>Образовательные результаты</h1>
        <div className="tooltip">
          <div className="block">
            <div className="pie">
              <Pie
                data={data}
              />
            </div>
          </div>
          <div className="block">
            <h2>Средняя оценка</h2>
            {(5 * score[5] + 4 * score[4] + 3 * score[3] + 2 * score[2]) / Object.values(score).reduce((ac, sc) => ac + sc)}
          </div>
          <div className="block2">
            <h2 style={{
              textAlign: "center"
            }}>Общие данные</h2>
            <div>URL репозитория: {location.state.github_url}</div>
            <div>Дата время проверки: {location.state.created_at}</div>
            <Button variant="outlined" onClick={() => navigate("/solution-all")} >Посмотреть прошлые результаты</Button>
          </div>
        </div>
        <TableContainer component={Paper}>
          <Table sx={{ minWidth: 650 }} aria-label="simple table">
            <TableHead>
              <TableRow>
                <TableCell>Образовательный результат</TableCell>
                <TableCell align="right">Уровень</TableCell>
                <TableCell align="right">Необходимо повторить или изучить</TableCell>
                <TableCell align="right">Номера задач для практики</TableCell>
              </TableRow>
            </TableHead>
            <TableBody>
              {
                location.state.learning_outcomes.map((row) => (
                  <TableRow
                    key={row.name}
                    sx={{ '&:last-child td, &:last-child th': { border: 0 } }}
                  >
                    <TableCell component="th" scope="row">
                      {row.name}
                    </TableCell>
                    <TableCell align="right">{row.score}</TableCell>
                    <TableCell align="right">
                      {row.recommendations.map((recommendation) => <div>{recommendation.name}</div>)}
                    </TableCell>
                    <TableCell align="right">
                      {
                        row.recommendations.map((recommendation) => <div>{recommendation.task}</div>)
                      }
                    </TableCell>
                  </TableRow>
                ))}
            </TableBody>
          </Table>
        </TableContainer>
      </div>
    </div>
  );
}

export default Solution;
