import noti from './Notice.module.css';
//게시판 글 양식

function Notice(){
    return (
        <div className={noti.Notice}>
          <h1>글 작성</h1>
          <div className={noti.movie_container}>
            <h2>제목</h2>
            <div>
              내용
            </div>
          </div>
          <div className={noti.form_wrapper}>
            <input className={noti.title_input} type='text' placeholder='제목' />
            <textarea className={noti.text_area} placeholder='내용'></textarea>
          </div>
        <button className={noti.submit_button}>입력</button>
        </div>
      );


}

export default Notice;