// import './App.css';
import { BrowserRouter, Routes, Route} from "react-router-dom";
import Login from './component/login/login';
import Home from './component/home/home';
import NoPage from './component/NoPage/NoPage';
function App() {
  return (
    <BrowserRouter>
    <Routes>
      <Route path='/' element={<Login />} />
      <Route path='/home' element={<Home />} />
      <Route path='*' element={<NoPage />}/>
    </Routes>
    </BrowserRouter>
  );
}

export default App;
