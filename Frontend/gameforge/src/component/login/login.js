import './login.css'
import myImage from './static/GameForgelogo.png';
import { Link } from 'react-router-dom';
function Login(){
    return(
        <div className='main'>
            <div className="login-main">
                <div className='login-top'>
                    <div className='top-items'>
                        <div className='logo-img'>
                            <img src={myImage} alt='Logo' className='logo'/> 
                            <h3 className='logo-text'>Welcome Back</h3>
                        </div>
                        <div className='logo-info'>
                            <p>Please enter your details to sign in</p>
                        </div>
                    </div>
                    <div className='down-items'> 
                        <div className='Google'><img src='https://www.google.com/images/hpp/ic_wahlberg_product_core_48.png8.png' alt='google' className='logo-g'/></div>
                        <div className='Google'><img src='https://www.google.com/images/hpp/ic_wahlberg_product_core_48.png8.png'  alt='google' className='logo-g'/></div>
                        <div className='Google'><img src='https://www.google.com/images/hpp/ic_wahlberg_product_core_48.png8.png' alt='google' className='logo-g'/></div>
                    </div>
                </div>
                <div className='login-middle'> or</div>
                <div className="login-bottom">
                    <form className="login-forms">
                        <label>E-Mail Address</label><br />
                        <input className='type1' type='text' placeholder="Enter your Email" required/><br />
                        <label>Password</label><br />
                        <input className='type1' type='password' placeholder="Enter Password" required/><br />
                        <div className='login-signup'>
                            <div className='left'>
                                <input type='checkbox' /> <label>Remember me</label>
                            </div>
                            <div className='right'>
                                <Link>Forget Password?</Link>
                            </div>
                        </div>
                        <input type='submit' className='button' value='Sign in' />
                        <p>Don't have an account yet? <Link>Sign up </Link></p>
                    </form>
                </div>
            </div>
        </div>
    );
}
export default Login;
