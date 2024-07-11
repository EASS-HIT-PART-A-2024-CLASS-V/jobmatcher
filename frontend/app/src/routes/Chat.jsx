import styles from '../styles/Chat.module.css';
import { useNavigate } from "react-router-dom";
import Button from '../components/Button';
export default function Chat({setIsMatch}) {
    const navigate =  useNavigate()
    const handleBackClick = () => {
        navigate(-1);
      };
    
      return (
        <div className={styles.container}>
          <h1 className={styles.message}>Oops, this feature is in development.</h1>
          <Button onClick={handleBackClick} caption="Back to Swiping" className={styles.button} />
        </div>
      );
}