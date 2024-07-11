import styles from '../styles/Chat.module.css';

export default function Chat({setIsMatch}) {
    const handleBackClick = () => {
        setIsMatch(false);
      };
    
      return (
        <div className={styles.container}>
          <h1 className={styles.message}>Oops, this feature is in development.</h1>
          {/* <Button onClick={handleBackClick} caption="Back to Swiping" className={styles.button} /> */}
        </div>
      );
}