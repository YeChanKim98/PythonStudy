import logging
import logging as lg

# 로그 포멧 설정 : 로그 작성의 기준은 디버그 레벨로 지정(지정 이상 레벨은 다 출력)
# 로그 레벨 순위 : Debug < Info < Warning < Error < Critical
lg.basicConfig(level=logging.DEBUG, format='%(asctime)s [%(levelname)s] %(message)s')
lg.debug('Here Point 001') # 개발자가 개발중 내부에 찍기 위해
lg.info('Testing') # 밖으로 출력하여 유저도 볼 수 있음
lg.warning('Warning') # 사용자에게도 Warning 양식으로 출력
lg.error('Error') # 사용자에게도 Error 양식으로 출력
lg.critical('Critical') # 사용자에게도 Critical 양식으로 출력

# 핸들러를 추가하여, 스트림(터미널) 및 파일에 로그를 남긴다
logFormat = lg.basicConfig(level=logging.DEBUG, format='%(asctime)s [%(levelname)s] %(message)s')
logger = lg.getLogger() # 로그를 찍는 로거 객체
logger.setLevel(logging.DEBUG) # 로깅 레벨 설정
stream_h = lg.StreamHandler() # 스트림 핸들러 객체
stream_h.setFormatter(logFormat) # 스트림 핸들러 객체에 포멧 지정
logger.addHandler(stream_h) # 로거에 스트림핸들러 추가
filename = 'log_file.txt'
file = lg.FileHandler(filename,encoding='utf-8') # 파일핸들러 객체 설정
file.setFormatter(logFormat) # 파일핸들러 포맷 지정
logger.addHandler(file) # 로거에 파일핸들러 추가

lg.debug('Here Point 001') # 개발자가 개발중 내부에 찍기 위해
lg.info('Testing') # 밖으로 출력하여 유저도 볼 수 있음
lg.warning('Warning') # 사용자에게도 Warning 양식으로 출력
lg.error('Error') # 사용자에게도 Error 양식으로 출력
lg.critical('Critical') # 사용자에게도 Critical 양식으로 출력
