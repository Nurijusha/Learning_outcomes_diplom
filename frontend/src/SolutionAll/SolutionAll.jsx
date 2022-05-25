import React, { useEffect, useMemo, useState } from "react";
import Button from '@mui/material/Button';
import {
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

import {
  Chart as ChartJS,
  CategoryScale,
  LinearScale,
  PointElement,
  LineElement,
  Title,
  Tooltip,
  Legend,
  BarElement,
} from 'chart.js';
import { Line, Bar } from 'react-chartjs-2';

import { getScore } from "../helpers";

ChartJS.register(
  CategoryScale,
  LinearScale,
  PointElement,
  LineElement,
  BarElement,
  Title,
  Tooltip,
  Legend
);

const init_score = {
  5: 0,
  4: 0,
  3: 0,
  2: 0
}

function SolutionAll() {
  const [solutions, setSolutions] = useState([]);
  const [score, setScore] = useState({
    5: 0,
    4: 0,
    3: 0,
    2: 0
  });
  useEffect(() => {
    fetch(`/api/solutions/`, {
      method: "GET",
      headers: new Headers({
        'Authorization': `Token ${sessionStorage.getItem('auth_token')}`,
      }),
    })
      .then((response) => {
        response.json().then(value => {
          setSolutions(value)
          const newscore = Object.assign({}, init_score);
          value[0].learning_outcomes.map((value) => newscore[value.score] = newscore[value.score] + 1);
          setScore(newscore)
        })
      })
  }, [])

  const labels = solutions.reverse().map(solution => new Date(solution.created_at).toLocaleDateString());

  const options = {
    scales: {
      yAxis: {
        min: 0,
        max: 5,
      }
    }
  };

  const data = useMemo(() => {
    return {
      labels,
      datasets: [
        {
          label: 'Dataset 1',
          data: solutions.reverse().map((solution) => {
            const newscore = {
              5: 0,
              4: 0,
              3: 0,
              2: 0
            }
            solution.learning_outcomes.map((value) => newscore[value.score] = newscore[value.score] + 1);
            return (getScore(newscore))
          }),
          borderColor: 'green',
          backgroundColor: 'green',
        },
      ],
    };
  }, [solutions])

  const data2 = useMemo(() => {
    return {
      labels: solutions[0]?.learning_outcomes.map((_, i) => String(i + 1)),
      datasets: [
        {
          label: 'текущая оценка',
          data: solutions[0]?.learning_outcomes.map(solution => solution.score),
          borderColor: 'blue',
          backgroundColor: 'blue',
        },
        {
          label: 'прошлая оценка',
          data: solutions[1]?.learning_outcomes.map(solution => solution.score),
          borderColor: 'red',
          backgroundColor: 'red',
        }
      ],
    };
  }, [solutions])

  return (
    <div className="contentCenter" >
      <div className="solution">
        <h1>Образовательные результаты</h1>
        <div className="tooltip">
          <div className="block">
            <Line
              options={options}
              data={data}
            />
          </div>
          <div className="block">
            <Bar
              options={options}
              data={data2}
            />
          </div>
          <div className="block">
            <h2>Средняя оценка</h2>
            {getScore(score)}
            <div>URL {solutions[0]?.github_url}</div>
          </div>
        </div>
        <TableContainer component={Paper}>
          <Table sx={{ minWidth: 650 }} aria-label="simple table">
            <TableHead>
              <TableRow>
                <TableCell>ID</TableCell>
                <TableCell>Образовательный результат</TableCell>
                {
                  solutions.map((_) => (
                    <>
                      <TableCell align="right">Дата/время</TableCell>
                      <TableCell align="right">Уровень</TableCell>
                    </>
                  ))
                }
              </TableRow>
            </TableHead>
            <TableBody>
              {
                solutions[0]?.learning_outcomes.map((learning_outcome, i) => (
                  <TableRow
                    key={learning_outcome.name}
                    sx={{ '&:last-child td, &:last-child th': { border: 0 } }}
                  >
                    <>
                      <TableCell align="right">{i + 1}</TableCell>
                      <TableCell align="right">{learning_outcome.name}</TableCell>
                      {
                        solutions.map(solution => (
                          <>
                            <TableCell align="right">{new Date(solution?.created_at).toLocaleString()}</TableCell>
                            <TableCell align="right">{solution.learning_outcomes[i]?.score}</TableCell>
                          </>
                        ))
                      }
                    </>
                  </TableRow>
                ))}
            </TableBody>
          </Table>
        </TableContainer>
      </div>
    </div >
  );
}

export default SolutionAll;
