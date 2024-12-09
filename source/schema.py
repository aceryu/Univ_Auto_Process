#!/usr/bin/env python
# # coding: utf-8

#################################################
# 테이블 스키마 정의
# 스키마가 변경되면 VS 리스타트
#################################################
table_dic = {}

# 학교 코드 정보 테이블
# table_dic['university'] = \
#     "CREATE TABLE `university` (\
#     `univ_cd` varchar(10) NOT NULL COMMENT '대학 고유코드',\
#     `univ_name_arlimi` varchar(100) DEFAULT NULL COMMENT '대학명(알리미기준)',\
#     `univ_name` varchar(100) NOT NULL COMMENT '대학명(일반명칭)',\
#     `univ_name_en` varchar(100) NOT NULL COMMENT '대학명(영문)',\
#     `univ_type` varchar(200) NOT NULL COMMENT '학교종류',\
#     `establish` varchar(10) NOT NULL COMMENT '설립구분',\
#     `status` varchar(10) NOT NULL COMMENT '상태',\
#     `campus` varchar(10) NOT NULL COMMENT '캠퍼스',\
#     `campus_name` varchar(200) NOT NULL COMMENT '캠퍼스명',\
#     `locale` varchar(10) NOT NULL COMMENT '지역',\
#     `homepage` varchar(200) NOT NULL COMMENT '학교 홈페이지',\
#     `tel` varchar(20) NOT NULL COMMENT '전화번호',\
#     `fax` varchar(20) NOT NULL COMMENT '팩스번호',\
#     `reg_date` datetime DEFAULT CURRENT_TIMESTAMP COMMENT '생성일시',\
#     `mod_date` datetime DEFAULT NULL COMMENT '수정일시',\
#     PRIMARY KEY (`univ_cd`)\
#     ) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COMMENT='대학교정보';"
# table_dic['대학교정보'] = 'university'

# 학교 코드 정보 테이블 - 240325
table_dic['university'] = \
    "CREATE TABLE `university` (\
    `univ_cd` varchar(10) NOT NULL COMMENT '학교코드',\
    `univ_name_arlimi` varchar(100) DEFAULT NULL COMMENT '학교명(알리미기준)',\
    `univ_type` varchar(50) DEFAULT NULL COMMENT '대학구분',\
    `scale` varchar(10) DEFAULT NULL COMMENT '대학규모',\
    `locale` varchar(10) DEFAULT NULL COMMENT '지역',\
    `locale_detail` varchar(50) DEFAULT NULL COMMENT '지역(상세)',\
    `establish` varchar(10) DEFAULT NULL COMMENT '설립구분',\
    `univ_name` varchar(100) DEFAULT NULL COMMENT '학교명(별칭)',\
    `univ_name_en` varchar(100) DEFAULT NULL COMMENT '학교명(영문)',\
    `campus` varchar(10) DEFAULT NULL COMMENT '캠퍼스',\
    `campus_name` varchar(50) DEFAULT NULL COMMENT '캠퍼스명',\
    `corporate_name` varchar(50) DEFAULT NULL COMMENT '법인명',\
    `status` varchar(10) DEFAULT NULL COMMENT '상태',\
    `founding` varchar(20) DEFAULT NULL COMMENT '개교일',\
    `closing` varchar(20) DEFAULT NULL COMMENT '폐교일',\
    `homepage` varchar(50) DEFAULT NULL COMMENT '학교 홈페이지',\
    `tel` varchar(20) DEFAULT NULL COMMENT '전화번호',\
    `fax` varchar(20) DEFAULT NULL COMMENT '팩스번호',\
    `remark` varchar(200) DEFAULT NULL COMMENT '비고',\
    `reg_date` datetime DEFAULT current_timestamp() COMMENT '생성일시',\
    `mod_date` datetime DEFAULT NULL COMMENT '수정일시',\
    PRIMARY KEY (`univ_cd`)\
    ) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci COMMENT='대학교정보';"
table_dic['대학교정보'] = 'university'


table_dic['kuai_tuition_and_reimbursement'] = \
    "CREATE TABLE `kuai_tuition_and_reimbursement` (\
    `year` int(4) NOT NULL COMMENT '기준연도',\
    `univ_cd` varchar(10) NOT NULL COMMENT '대학 고유코드',\
    `tuition_fee_tot` bigint(20) COMMENT '총교육비(원)',\
    `tuition_fee` bigint(20) COMMENT '등록금(원)',\
    `tuition_fee_reimbursement_rate` float(8, 2) DEFAULT 0.00 COMMENT '교육비 환원율', \
    `reg_date` datetime DEFAULT CURRENT_TIMESTAMP COMMENT '생성일시',\
    `mod_date` datetime DEFAULT NULL COMMENT '수정일시',\
    PRIMARY KEY (`year`,`univ_cd`),\
    KEY `univ_cd` (`univ_cd`),\
    CONSTRAINT `kuai_tuition_and_reimbursement_ibfk_1` FOREIGN KEY (`univ_cd`) REFERENCES `university` (`univ_cd`)\
    ) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COMMENT='KUAI_교육비 환원율 지표';"
table_dic['KUAI_교육비 환원율 지표'] = 'kuai_tuition_and_reimbursement'



# 중도탈락 현황 테이블(수동으로 통합 변경된 테이블)
table_dic['dropout_stat'] = \
    "CREATE TABLE `dropout_stat` (\
    `year` int(4) NOT NULL COMMENT '기준연도',\
    `univ_cd` varchar(10) NOT NULL COMMENT '대학 고유코드',\
    `stud_tot` int(6) DEFAULT 0 COMMENT '재적_학생수',\
    `stud_sum` int(6) DEFAULT 0 COMMENT '재적_중도탈락_합계',\
    `stud_unregist` int(6) DEFAULT 0 COMMENT '재적_중도탈락_미등록',\
    `stud_unreturn` int(6) DEFAULT 0 COMMENT '재적_중도탈락_미복학',\
    `stud_drop` int(6) DEFAULT 0 COMMENT '재적_중도탈락_자퇴',\
    `stud_warn` int(6) DEFAULT 0 COMMENT '재적_중도탈락_학사경고',\
    `stud_act` int(6) DEFAULT 0 COMMENT '재적_중도탈락_학생활동',\
    `stud_expulsion` int(6) DEFAULT 0 COMMENT '재적_중도탈락_유급제적',\
    `stud_attendyear` int(6) DEFAULT 0 COMMENT '재적_중도탈락_재학연한초과',\
    `stud_etc` int(6) DEFAULT 0 COMMENT '재적_중도탈락_기타',\
    `stud_rate` float(5,2) DEFAULT 0.00 COMMENT '재적_중도탈락_비율',\
    `fresh_tot` int(6) DEFAULT 0 COMMENT '신입_학생수',\
    `fresh_sum` int(6) DEFAULT 0 COMMENT '신입_중도탈락_합계',\
    `fresh_unregist` int(6) DEFAULT 0 COMMENT '신입_중도탈락_미등록',\
    `fresh_unreturn` int(6) DEFAULT 0 COMMENT '신입_중도탈락_미복학',\
    `fresh_drop` int(6) DEFAULT 0 COMMENT '신입_중도탈락_자퇴',\
    `fresh_warn` int(6) DEFAULT 0 COMMENT '신입_중도탈락_학사경고',\
    `fresh_act` int(6) DEFAULT 0 COMMENT '신입_중도탈락_학생활동',\
    `fresh_expulsion` int(6) DEFAULT 0 COMMENT '신입_중도탈락_유급제적',\
    `fresh_attendyear` int(6) DEFAULT 0 COMMENT '신입_중도탈락_재학연한초과',\
    `fresh_etc` int(6) DEFAULT 0 COMMENT '신입_중도탈락_기타',\
    `fresh_rate` float(5,2) DEFAULT 0.00 COMMENT '신입_중도탈락_비율',\
    `foreign_tot` int(6) DEFAULT 0 COMMENT '외국인_학생수',\
    `foreign_sum` int(6) DEFAULT 0 COMMENT '외국인_중도탈락_합계',\
    `foreign_degree` int(6) DEFAULT 0 COMMENT '외국인_학위과정(대학)',\
    `foreign_common` int(6) DEFAULT 0 COMMENT '외국인_교육과정공동운영생',\
    `foreign_lang` int(6) DEFAULT 0 COMMENT '외국인_어학연수생',\
    `foreign_exchange` int(6) DEFAULT 0 COMMENT '외국인_교환학생',\
    `foreign_visit` int(6) DEFAULT 0 COMMENT '외국인_방문학생',\
    `foreign_etc` int(6) DEFAULT 0 COMMENT '외국인_기타연수생',\
    `foreign_rate` float(5,2) DEFAULT 0.00 COMMENT '외국인_중도탈락_비율',\
    `reg_date` datetime DEFAULT CURRENT_TIMESTAMP COMMENT '생성일시',\
    `mod_date` datetime DEFAULT NULL COMMENT '수정일시',\
    PRIMARY KEY (`year`,`univ_cd`),\
    KEY `univ_cd` (`univ_cd`),\
    CONSTRAINT `dropout_ibfk_1` FOREIGN KEY (`univ_cd`) REFERENCES `university` (`univ_cd`)\
    ) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COMMENT='중도탈락 학생 현황';"
table_dic['중도탈락 학생 현황(통합)'] = 'dropout_stat'        
    
# 2023년_ [2-가-1. 전공과목 성적 분포_] 테이블
#################################################
# 테이블명 : major_grades | 전공과목 성적 분포
# 필드 : year    | DEL      | DEL     | DEL  | DEL | DEL    | semester | stud_tot                 | perfect_rating  | stud_A+   | rate_A+ | stud_A0 | rate_A0  | stud_B+  | rate_B+ | stud_B0 | rate_B0  | stud_C+ | rate_C+ | stud_C0 | rate_C0   | stud_D+  | rate_D+ | stud_D0 | rate_D0  | stud_F   | rate_F
# 설명 : 기준연도 | 학교종류 | 설립구분 | 지역 | 상태 | 학교명 | 학기      | 전공과목 성적인정 총학생수 | 만점평점         | A+ 학생수 | A+ 비율 | A0 학생수 | A0 비율 | B+ 학생수 | B+ 비율 | B0 학생수 | B0 비율 | C+ 학생수 | C+ 비율 | C0 학생수 | C0 비율 | D+ 학생수 | D+ 비율 | D0 학생수 | D0 비율 | F 학생수 | F 비율 
#################################################
table_dic['major_grades'] = \
    "CREATE TABLE `major_grades` (\
    `year` int(4) NOT NULL COMMENT '기준연도',\
    `univ_cd` varchar(10) NOT NULL COMMENT '대학 고유코드',\
    `semester` varchar(10) NOT NULL COMMENT '학기',\
    `stud_tot` int(6) DEFAULT 0 COMMENT '전공과목 성적인정 총학생수',\
    `perfect_rating` float(5,2) DEFAULT 0 COMMENT '만점평점',\
    `stud_Ap` int(6) DEFAULT 0 COMMENT 'A+ 학생수',\
    `rate_Ap` float(5,2) DEFAULT 0.00 COMMENT 'A+ 비율',\
    `stud_A0` int(6) DEFAULT 0 COMMENT 'A0 학생수',\
    `rate_A0` float(5,2) DEFAULT 0.00 COMMENT 'A0 비율',\
    `stud_Bp` int(6) DEFAULT 0 COMMENT 'B+ 학생수',\
    `rate_Bp` float(5,2) DEFAULT 0.00 COMMENT 'B+ 비율',\
    `stud_B0` int(6) DEFAULT 0 COMMENT 'B0 학생수',\
    `rate_B0` float(5,2) DEFAULT 0.00 COMMENT 'B0 비율',\
    `stud_Cp` int(6) DEFAULT 0 COMMENT 'C+ 학생수',\
    `rate_Cp` float(5,2) DEFAULT 0.00 COMMENT 'C+ 비율',\
    `stud_C0` int(6) DEFAULT 0 COMMENT 'C0 학생수',\
    `rate_C0` float(5,2) DEFAULT 0.00 COMMENT 'C0 비율',\
    `stud_Dp` int(6) DEFAULT 0 COMMENT 'D+ 학생수',\
    `rate_Dp` float(5,2) DEFAULT 0.00 COMMENT 'D+ 비율',\
    `stud_D0` int(6) DEFAULT 0 COMMENT 'D0 학생수',\
    `rate_D0` float(5,2) DEFAULT 0.00 COMMENT 'D0 비율',\
    `stud_F` int(6) DEFAULT 0 COMMENT 'F 학생수',\
    `rate_F` float(5,2) DEFAULT 0.00 COMMENT 'F 비율',\
    `reg_date` datetime DEFAULT CURRENT_TIMESTAMP COMMENT '생성일시',\
    `mod_date` datetime DEFAULT NULL COMMENT '수정일시',\
    PRIMARY KEY (`year`,`univ_cd`, `semester`),\
    KEY `univ_cd` (`univ_cd`),\
    CONSTRAINT `major_grades_ibfk_1` FOREIGN KEY (`univ_cd`) REFERENCES `university` (`univ_cd`)\
    ) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COMMENT='전공과목 성적 분포';"
table_dic['전공과목 성적 분포'] = 'major_grades'


# 2023년_ [2-가-2. 교양과목 성적 분포_] 테이블
#################################################
# 테이블명 : liberal_arts_grades | 교양과목 성적 분포
# 필드 : year    | DEL      | DEL     | DEL  | DEL | DEL    | semester | stud_tot                 | perfect_rating  | stud_A+   | rate_A+ | stud_A0 | rate_A0  | stud_B+  | rate_B+ | stud_B0 | rate_B0  | stud_C+ | rate_C+ | stud_C0 | rate_C0   | stud_D+  | rate_D+ | stud_D0 | rate_D0  | stud_F   | rate_F
# 설명 : 기준연도 | 학교종류 | 설립구분 | 지역 | 상태 | 학교명 | 학기      | 교양과목 성적인정 총학생수 | 만점평점         | A+ 학생수 | A+ 비율 | A0 학생수 | A0 비율 | B+ 학생수 | B+ 비율 | B0 학생수 | B0 비율 | C+ 학생수 | C+ 비율 | C0 학생수 | C0 비율 | D+ 학생수 | D+ 비율 | D0 학생수 | D0 비율 | F 학생수 | F 비율 
#################################################
table_dic['liberal_arts_grades'] = \
    "CREATE TABLE `liberal_arts_grades` (\
    `year` int(4) NOT NULL COMMENT '기준연도',\
    `univ_cd` varchar(10) NOT NULL COMMENT '대학 고유코드',\
    `semester` varchar(10) NOT NULL COMMENT '학기',\
    `stud_tot` int(6) DEFAULT 0 COMMENT '교양과목 성적인정 총학생수',\
    `perfect_rating` float(5,2) DEFAULT 0 COMMENT '만점평점',\
    `stud_Ap` int(6) DEFAULT 0 COMMENT 'A+ 학생수',\
    `rate_Ap` float(5,2) DEFAULT 0.00 COMMENT 'A+ 비율',\
    `stud_A0` int(6) DEFAULT 0 COMMENT 'A0 학생수',\
    `rate_A0` float(5,2) DEFAULT 0.00 COMMENT 'A0 비율',\
    `stud_Bp` int(6) DEFAULT 0 COMMENT 'B+ 학생수',\
    `rate_Bp` float(5,2) DEFAULT 0.00 COMMENT 'B+ 비율',\
    `stud_B0` int(6) DEFAULT 0 COMMENT 'B0 학생수',\
    `rate_B0` float(5,2) DEFAULT 0.00 COMMENT 'B0 비율',\
    `stud_Cp` int(6) DEFAULT 0 COMMENT 'C+ 학생수',\
    `rate_Cp` float(5,2) DEFAULT 0.00 COMMENT 'C+ 비율',\
    `stud_C0` int(6) DEFAULT 0 COMMENT 'C0 학생수',\
    `rate_C0` float(5,2) DEFAULT 0.00 COMMENT 'C0 비율',\
    `stud_Dp` int(6) DEFAULT 0 COMMENT 'D+ 학생수',\
    `rate_Dp` float(5,2) DEFAULT 0.00 COMMENT 'D+ 비율',\
    `stud_D0` int(6) DEFAULT 0 COMMENT 'D0 학생수',\
    `rate_D0` float(5,2) DEFAULT 0.00 COMMENT 'D0 비율',\
    `stud_F` int(6) DEFAULT 0 COMMENT 'F 학생수',\
    `rate_F` float(5,2) DEFAULT 0.00 COMMENT 'F 비율',\
    `reg_date` datetime DEFAULT CURRENT_TIMESTAMP COMMENT '생성일시',\
    `mod_date` datetime DEFAULT NULL COMMENT '수정일시',\
    PRIMARY KEY (`year`,`univ_cd`, `semester`),\
    KEY `univ_cd` (`univ_cd`),\
    CONSTRAINT `liberal_arts_grades_ibfk_1` FOREIGN KEY (`univ_cd`) REFERENCES `university` (`univ_cd`)\
    ) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COMMENT='교양과목 성적 분포';"
table_dic['교양과목 성적 분포'] = 'liberal_arts_grades'


# 2023년_ [2-가-3. 교직과목 성적 분포_] 테이블
#################################################
# 테이블명 : teaching_profession_grades | 교직과목 성적 분포
# 필드 : year    | DEL      | DEL     | DEL  | DEL | DEL    | semester | stud_tot                 | perfect_rating  | stud_A+   | rate_A+ | stud_A0 | rate_A0  | stud_B+  | rate_B+ | stud_B0 | rate_B0  | stud_C+ | rate_C+ | stud_C0 | rate_C0   | stud_D+  | rate_D+ | stud_D0 | rate_D0  | stud_F   | rate_F
# 설명 : 기준연도 | 학교종류 | 설립구분 | 지역 | 상태 | 학교명 | 학기      | 교직과목 성적인정 총학생수 | 만점평점         | A+ 학생수 | A+ 비율 | A0 학생수 | A0 비율 | B+ 학생수 | B+ 비율 | B0 학생수 | B0 비율 | C+ 학생수 | C+ 비율 | C0 학생수 | C0 비율 | D+ 학생수 | D+ 비율 | D0 학생수 | D0 비율 | F 학생수 | F 비율 
#################################################
table_dic['teaching_profession_grades'] = \
    "CREATE TABLE `teaching_profession_grades` (\
    `year` int(4) NOT NULL COMMENT '기준연도',\
    `univ_cd` varchar(10) NOT NULL COMMENT '대학 고유코드',\
    `semester` varchar(10) NOT NULL COMMENT '학기',\
    `stud_tot` int(6) DEFAULT 0 COMMENT '교직과목 성적인정 총학생수',\
    `perfect_rating` float(5,2) DEFAULT 0 COMMENT '만점평점',\
    `stud_Ap` int(6) DEFAULT 0 COMMENT 'A+ 학생수',\
    `rate_Ap` float(5,2) DEFAULT 0.00 COMMENT 'A+ 비율',\
    `stud_A0` int(6) DEFAULT 0 COMMENT 'A0 학생수',\
    `rate_A0` float(5,2) DEFAULT 0.00 COMMENT 'A0 비율',\
    `stud_Bp` int(6) DEFAULT 0 COMMENT 'B+ 학생수',\
    `rate_Bp` float(5,2) DEFAULT 0.00 COMMENT 'B+ 비율',\
    `stud_B0` int(6) DEFAULT 0 COMMENT 'B0 학생수',\
    `rate_B0` float(5,2) DEFAULT 0.00 COMMENT 'B0 비율',\
    `stud_Cp` int(6) DEFAULT 0 COMMENT 'C+ 학생수',\
    `rate_Cp` float(5,2) DEFAULT 0.00 COMMENT 'C+ 비율',\
    `stud_C0` int(6) DEFAULT 0 COMMENT 'C0 학생수',\
    `rate_C0` float(5,2) DEFAULT 0.00 COMMENT 'C0 비율',\
    `stud_Dp` int(6) DEFAULT 0 COMMENT 'D+ 학생수',\
    `rate_Dp` float(5,2) DEFAULT 0.00 COMMENT 'D+ 비율',\
    `stud_D0` int(6) DEFAULT 0 COMMENT 'D0 학생수',\
    `rate_D0` float(5,2) DEFAULT 0.00 COMMENT 'D0 비율',\
    `stud_F` int(6) DEFAULT 0 COMMENT 'F 학생수',\
    `rate_F` float(5,2) DEFAULT 0.00 COMMENT 'F 비율',\
    `reg_date` datetime DEFAULT CURRENT_TIMESTAMP COMMENT '생성일시',\
    `mod_date` datetime DEFAULT NULL COMMENT '수정일시',\
    PRIMARY KEY (`year`,`univ_cd`, `semester`),\
    KEY `univ_cd` (`univ_cd`),\
    CONSTRAINT `teaching_profession_grades_ibfk_1` FOREIGN KEY (`univ_cd`) REFERENCES `university` (`univ_cd`)\
    ) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COMMENT='교직과목 성적 분포';"
table_dic['교직과목 성적 분포'] = 'teaching_profession_grades'



# 2023년_ [2-가-4. 졸업생의 졸업성적 분포_]
#################################################
# 테이블명 : graduate_grades | 졸업생의 졸업성적 분포
# 필드 : year    | DEL      | DEL     | DEL  | DEL | DEL   | send_tot        | send_0_3            | send_3_6           | send_6_12           | send_12          | receive_tot        | receive_0_3            | receive_3_6           | receive_6_12           | receive_12
#################################################
table_dic['graduate_grades'] = \
    "CREATE TABLE `graduate_grades` (\
    `year` int(4) NOT NULL COMMENT '기준연도',\
    `univ_cd` varchar(10) NOT NULL COMMENT '대학 고유코드',\
    `graduate_tot` varchar(200) COMMENT '졸업자 수',\
    `department_avg_grade` varchar(200) COMMENT '학과(전공) 별 졸업평점 평균',\
    `perfect_rating` varchar(200) COMMENT '만점평점',\
    `department_avg_rate` varchar(200) COMMENT '학과(전공) 별 졸업 백분율 점수 평균',\
    `grade_100_95` int(6) DEFAULT 0 COMMENT '평점(점수구간)별 학생수(대학에서 정한 학업성적 등급)_100_95',\
    `rate_100_95` float(8, 2) DEFAULT 0.00 COMMENT '평점(점수구간)별 비율(대학에서 정한 학업성적 등급)_100_95',\
    `grade_95_90` int(6) DEFAULT 0 COMMENT '평점(점수구간)별 학생수(대학에서 정한 학업성적 등급)_95_90',\
    `rate_95_90` float(8, 2) DEFAULT 0.00 COMMENT '평점(점수구간)별 비율(대학에서 정한 학업성적 등급)_95_90',\
    `grade_90_85` int(6) DEFAULT 0 COMMENT '평점(점수구간)별 학생수(대학에서 정한 학업성적 등급)_90_85',\
    `rate_90_85` float(8, 2) DEFAULT 0.00 COMMENT '평점(점수구간)별 비율(대학에서 정한 학업성적 등급)_90_85',\
    `grade_85_80` int(6) DEFAULT 0 COMMENT '평점(점수구간)별 학생수(대학에서 정한 학업성적 등급)_85_80',\
    `rate_85_80` float(8, 2) DEFAULT 0.00 COMMENT '평점(점수구간)별 비율(대학에서 정한 학업성적 등급)_85_80',\
    `grade_80_75` int(6) DEFAULT 0 COMMENT '평점(점수구간)별 학생수(대학에서 정한 학업성적 등급)_80_75',\
    `rate_80_75` float(8, 2) DEFAULT 0.00 COMMENT '평점(점수구간)별 비율(대학에서 정한 학업성적 등급)_80_75',\
    `grade_75_70` int(6) DEFAULT 0 COMMENT '평점(점수구간)별 학생수(대학에서 정한 학업성적 등급)_75_70',\
    `rate_75_70` float(8, 2) DEFAULT 0.00 COMMENT '평점(점수구간)별 비율(대학에서 정한 학업성적 등급)_75_70',\
    `grade_70_65` int(6) DEFAULT 0 COMMENT '평점(점수구간)별 학생수(대학에서 정한 학업성적 등급)_70_65',\
    `rate_70_65` float(8, 2) DEFAULT 0.00 COMMENT '평점(점수구간)별 비율(대학에서 정한 학업성적 등급)_70_65',\
    `grade_65_60` int(6) DEFAULT 0 COMMENT '평점(점수구간)별 학생수(대학에서 정한 학업성적 등급)_65_60',\
    `rate_65_60` float(8, 2) DEFAULT 0.00 COMMENT '평점(점수구간)별 비율(대학에서 정한 학업성적 등급)_65_60',\
    `grade_60` int(6) DEFAULT 0 COMMENT '평점(점수구간)별 학생수(대학에서 정한 학업성적 등급)_60미만',\
    `rate_60` float(8, 2) DEFAULT 0.00 COMMENT '평점(점수구간)별 비율(대학에서 정한 학업성적 등급)_60미만',\
    `reg_date` datetime DEFAULT CURRENT_TIMESTAMP COMMENT '생성일시',\
    `mod_date` datetime DEFAULT NULL COMMENT '수정일시',\
    PRIMARY KEY (`year`,`univ_cd`),\
    KEY `univ_cd` (`univ_cd`),\
    CONSTRAINT `graduate_grades_exchange_ibfk_1` FOREIGN KEY (`univ_cd`) REFERENCES `university` (`univ_cd`)\
    ) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COMMENT='졸업생의 졸업성적 분포';"
table_dic['졸업생의 졸업성적 분포'] = 'graduate_grades'





# 2023년_ [4-나. 기회 균형 선발 결과_]
#################################################
# 테이블명 : opportunity_select_results | 기회 균형 선발 결과
# 필드 : year    | DEL      | DEL     | DEL  | DEL | DEL   | completed_stud_dept | completed_stud_human_social | completed_stud_natural_science | completed_stud_engineering | completed_stud_medicine | support_amount_stud_tot | support_amount_prototype | support_amount_education |
# 설명 : 기준연도 | 학교종류 | 설립구분 | 지역 | 상태 | 학교명 | 이수학생수_해당학과 | 이수학생수_타학과_인문사회 | 이수학생수_타학과_자연과학 | 이수학생수_타학과_공학 | 이수학생수_타학과_의학 | 이수학생수_타학과_예체능 | 지원금수령_학생수(명) | 지원금수령_금액_시제품제작비 | 지원금수령_금액_교육프로그램지원비
#################################################
table_dic['opportunity_select_results'] = \
    "CREATE TABLE `opportunity_select_results` (\
    `year` int(4) NOT NULL COMMENT '기준연도',\
    `univ_cd` varchar(10) NOT NULL COMMENT '대학 고유코드',\
    `admission_tot` int(6) DEFAULT 0 COMMENT '전체 총 입학자',\
    `opportunity_tot` int(6) DEFAULT 0 COMMENT '기회균형 입학 합계(정원외소계+정원내소계)',\
    `out_recruitment_subtot` int(6) DEFAULT 0 COMMENT '정원외_소계',\
    `out_recruitment_basic_livelihood` int(6) DEFAULT 0 COMMENT '정원외_기초생활수급자',\
    `out_recruitment_second_lower` int(6) DEFAULT 0 COMMENT '정원외_차상위계층',\
    `out_recruitment_single_parent` int(6) DEFAULT 0 COMMENT '정원외_한부모가족 지원대상자',\
    `out_recruitment_special_school` int(6) DEFAULT 0 COMMENT '정원외_특성화고 졸업자',\
    `out_recruitment_special_school_graduate` int(6) DEFAULT 0 COMMENT '정원외_특성화고 등을 졸업한 재직자',\
    `out_recruitment_rural_student` int(6) DEFAULT 0 COMMENT '정원외_농어촌학생',\
    `out_recruitment_north_defector` int(6) DEFAULT 0 COMMENT '정원외_북한 이탈주민',\
    `out_recruitment_disabled` int(6) DEFAULT 0 COMMENT '정원외_장애인 등 대상자',\
    `out_recruitment_west_sea` int(6) DEFAULT 0 COMMENT '정원외_서해 5도 학생',\
    `out_recruitment_danwon_school` int(6) DEFAULT 0 COMMENT '정원외_단원고',\
    `in_recruitment_subtot` int(6) DEFAULT 0 COMMENT '정원내_소계',\
    `in_recruitment_opportunity` int(6) DEFAULT 0 COMMENT '정원내_고른기회 대상자',\
    `in_recruitment_univ_standard` int(6) DEFAULT 0 COMMENT '정원내_대학 독자적 기준',\
    `opportunity_rate` float(8, 2) DEFAULT 0.00 COMMENT '기회균형 선발 비율(합계/총입학자*100)',\
    `reg_date` datetime DEFAULT CURRENT_TIMESTAMP COMMENT '생성일시',\
    `mod_date` datetime DEFAULT NULL COMMENT '수정일시',\
    PRIMARY KEY (`year`,`univ_cd`),\
    KEY `univ_cd` (`univ_cd`),\
    CONSTRAINT `opportunity_select_results_ibfk_1` FOREIGN KEY (`univ_cd`) REFERENCES `university` (`univ_cd`)\
    ) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COMMENT='기회 균형 선발 결과';"
table_dic['기회 균형 선발 결과'] = 'opportunity_select_results'






# 2023년_ [12-라-2. 외국대학과 학점 교류 현황_]
#################################################
# 테이블명 : major_grades | 전공과목 성적 분포
# 필드 : year    | DEL      | DEL     | DEL  | DEL | DEL   | send_tot        | send_0_3            | send_3_6           | send_6_12           | send_12          | receive_tot        | receive_0_3            | receive_3_6           | receive_6_12           | receive_12
# 설명 : 기준연도 | 학교종류 | 설립구분 | 지역 | 상태 | 학교명 | 파견인원(자교->타교) | 파견기간별 인원(0<3개월) | 파견기간별 인원(3<6개월) | 파견기간별 인원(6<12개월) | 파견기간별 인원(12개월 이상) | 유치인원(타교->자교) | 유치기간별 인원(0<3개월) | 유치기간별 인원(3<6개월) | 유치기간별 인원(6<12개월) | 유치기간별 인원(12개월 이상) |
#################################################
table_dic['foreign_univ_grade_exchange'] = \
    "CREATE TABLE `foreign_univ_grade_exchange` (\
    `year` int(4) NOT NULL COMMENT '기준연도',\
    `univ_cd` varchar(10) NOT NULL COMMENT '대학 고유코드',\
    `send_tot` int(6) DEFAULT 0 COMMENT '파견인원(자교->타교)',\
    `send_0_3` int(6) DEFAULT 0 COMMENT '파견기간별 인원(0<3개월)',\
    `send_3_6` int(6) DEFAULT 0 COMMENT '파견기간별 인원(3<6개월)',\
    `send_6_12` int(6) DEFAULT 0 COMMENT '파견기간별 인원(6<12개월)',\
    `send_12` int(6) DEFAULT 0 COMMENT '파견기간별 인원(12개월 이상)',\
    `receive_tot` int(6) DEFAULT 0 COMMENT '유치인원(타교->자교)',\
    `receive_0_3` int(6) DEFAULT 0 COMMENT '유치기간별 인원(0<3개월)',\
    `receive_3_6` int(6) DEFAULT 0 COMMENT '유치기간별 인원(3<6개월)',\
    `receive_6_12` int(6) DEFAULT 0 COMMENT '유치기간별 인원(6<12개월)',\
    `sreceive_12` int(6) DEFAULT 0 COMMENT '유치기간별 인원(12개월 이상)',\
    `reg_date` datetime DEFAULT CURRENT_TIMESTAMP COMMENT '생성일시',\
    `mod_date` datetime DEFAULT NULL COMMENT '수정일시',\
    PRIMARY KEY (`year`,`univ_cd`),\
    KEY `univ_cd` (`univ_cd`),\
    CONSTRAINT `foreign_univ_grade_exchange_ibfk_1` FOREIGN KEY (`univ_cd`) REFERENCES `university` (`univ_cd`)\
    ) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COMMENT='외국대학과 학점 교류 현황';"
table_dic['외국대학과 학점 교류 현황'] = 'foreign_univ_grade_exchange'


# 2023년_ [12-카-1. 현장실습 운영 현황_]
#################################################
# 테이블명 : field_training | 현장실습 운영 현황
# 필드 : year    | DEL      | DEL     | DEL  | DEL | DEL   | ft_4w_tot | ft_4w_insure_wound | ft_4w_insure_industrial | ft_4w_fee_75p | ft_4w_fee_100p | ft_4w_home_25p_under | ft_4w_home_25p_above
# 설명 : 기준연도 | 학교종류 | 설립구분 | 지역 | 상태 | 학교명 | 실습기간_4주_이수학생수 | 실습기간_4주_보험가입_상해보험 | 실습기간_4주_보험가입_산재보험 | 실습기간_4주_실습지원비_75%이상 | 실습기간_4주_실습지원비_100%이상 | 실습기간_4주_재택실습이용학생_기간25%이하 | 실습기간_4주_재택실습이용학생_기간25%초과 
#                                                          | 실습기간_8주_이수학생수 | 실습기간_8주_보험가입_상해보험 | 실습기간_8주_보험가입_산재보험 | 실습기간_8주_실습지원비_75%이상 | 실습기간_8주_실습지원비_100%이상 | 실습기간_8주_재택실습이용학생_기간25%이하 | 실습기간_8주_재택실습이용학생_기간25%초과 
#                                                          | 실습기간_12주_이수학생수 | 실습기간_12주_보험가입_상해보험 | 실습기간_12주_보험가입_산재보험 | 실습기간_12주_실습지원비_75%이상 | 실습기간_12주_실습지원비_100%이상 | 실습기간_12주_재택실습이용학생_기간25%이하 | 실습기간_12주_재택실습이용학생_기간25%초과 
#################################################
table_dic['field_training'] = \
    "CREATE TABLE `field_training` (\
    `year` int(4) NOT NULL COMMENT '기준연도',\
    `univ_cd` varchar(10) NOT NULL COMMENT '대학 고유코드',\
    `ft_4w_tot` int(6) DEFAULT 0 COMMENT '실습기간_4주_이수학생수',\
    `ft_4w_insure_wound` int(6) DEFAULT 0 COMMENT '실습기간_4주_보험가입_상해보험',\
    `ft_4w_insure_industrial` int(6) DEFAULT 0 COMMENT '실습기간_4주_보험가입_산재보험',\
    `ft_4w_fee_75p` int(6) DEFAULT 0 COMMENT '실습기간_4주_실습지원비_75%이상',\
    `ft_4w_fee_100p` int(6) DEFAULT 0 COMMENT '실습기간_4주_실습지원비_100%이상',\
    `ft_4w_home_25p_under` int(6) DEFAULT 0 COMMENT '실습기간_4주_재택실습이용학생_기간25%이하',\
    `ft_4w_home_25p_above` int(6) DEFAULT 0 COMMENT '실습기간_4주_재택실습이용학생_기간25%초과',\
    `ft_8w_tot` int(6) DEFAULT 0 COMMENT '실습기간_8주_이수학생수',\
    `ft_8w_insure_wound` int(6) DEFAULT 0 COMMENT '실습기간_8주_보험가입_상해보험',\
    `ft_8w_insure_industrial` int(6) DEFAULT 0 COMMENT '실습기간_8주_보험가입_산재보험',\
    `ft_8w_fee_75p` int(6) DEFAULT 0 COMMENT '실습기간_8주_실습지원비_75%이상',\
    `ft_8w_fee_100p` int(6) DEFAULT 0 COMMENT '실습기간_8주_실습지원비_100%이상',\
    `ft_8w_home_25p_under` int(6) DEFAULT 0 COMMENT '실습기간_8주_재택실습이용학생_기간25%이하',\
    `ft_8w_home_25p_above` int(6) DEFAULT 0 COMMENT '실습기간_8주_재택실습이용학생_기간25%초과',\
    `ft_12w_tot` int(6) DEFAULT 0 COMMENT '실습기간_12주_이수학생수',\
    `ft_12w_insure_wound` int(6) DEFAULT 0 COMMENT '실습기간_12주_보험가입_상해보험',\
    `ft_12w_insure_industrial` int(6) DEFAULT 0 COMMENT '실습기간_12주_보험가입_산재보험',\
    `ft_12w_fee_75p` int(6) DEFAULT 0 COMMENT '실습기간_12주_실습지원비_75%이상',\
    `ft_12w_fee_100p` int(6) DEFAULT 0 COMMENT '실습기간_12주_실습지원비_100%이상',\
    `ft_12w_home_25p_under` int(6) DEFAULT 0 COMMENT '실습기간_12주_재택실습이용학생_기간25%이하',\
    `ft_12w_home_25p_above` int(6) DEFAULT 0 COMMENT '실습기간_12주_재택실습이용학생_기간25%초과',\
    `reg_date` datetime DEFAULT CURRENT_TIMESTAMP COMMENT '생성일시',\
    `mod_date` datetime DEFAULT NULL COMMENT '수정일시',\
    PRIMARY KEY (`year`,`univ_cd`),\
    KEY `univ_cd` (`univ_cd`),\
    CONSTRAINT `field_training_ibfk_1` FOREIGN KEY (`univ_cd`) REFERENCES `university` (`univ_cd`)\
    ) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COMMENT='현장실습 운영 현황';"
table_dic['현장실습 운영 현황'] = 'field_training'


# 2023년_ [12-카-2. 캡스톤 디자인(창의적 설계) 운영 현황_]
#################################################
# 테이블명 : capstone_design | 캡스톤 디자인(창의적 설계) 운영 현황
# 필드 : year    | DEL      | DEL     | DEL  | DEL | DEL   | completed_stud_dept | completed_stud_human_social | completed_stud_natural_science | completed_stud_engineering | completed_stud_medicine | completed_stud_art_sports | support_amount_stud_tot | support_amount_prototype | support_amount_education |
# 설명 : 기준연도 | 학교종류 | 설립구분 | 지역 | 상태 | 학교명 | 이수학생수_해당학과 | 이수학생수_타학과_인문사회 | 이수학생수_타학과_자연과학 | 이수학생수_타학과_공학 | 이수학생수_타학과_의학 | 이수학생수_타학과_예체능 | 지원금수령_학생수(명) | 지원금수령_금액_시제품제작비 | 지원금수령_금액_교육프로그램지원비
#################################################
table_dic['capstone_design'] = \
    "CREATE TABLE `capstone_design` (\
    `year` int(4) NOT NULL COMMENT '기준연도',\
    `univ_cd` varchar(10) NOT NULL COMMENT '대학 고유코드',\
    `completed_stud_dept` int(6) DEFAULT 0 COMMENT '이수학생수_해당학과',\
    `completed_stud_human_social` int(6) DEFAULT 0 COMMENT '이수학생수_타학과_인문사회',\
    `completed_stud_natural_science` int(6) DEFAULT 0 COMMENT '이수학생수_타학과_자연과학',\
    `completed_stud_engineering` int(6) DEFAULT 0 COMMENT '이수학생수_타학과_공학',\
    `completed_stud_medicine` int(6) DEFAULT 0 COMMENT '이수학생수_타학과_의학',\
    `completed_stud_art_sports` int(6) DEFAULT 0 COMMENT '이수학생수_타학과_예체능',\
    `support_amount_stud_tot` int(6) DEFAULT 0 COMMENT '지원금수령_학생수(명)',\
    `support_amount_prototype` int(6) DEFAULT 0 COMMENT '지원금수령_금액_시제품제작비',\
    `support_amount_education` int(6) DEFAULT 0 COMMENT '지원금수령_금액_교육프로그램지원비',\
    `reg_date` datetime DEFAULT CURRENT_TIMESTAMP COMMENT '생성일시',\
    `mod_date` datetime DEFAULT NULL COMMENT '수정일시',\
    PRIMARY KEY (`year`,`univ_cd`),\
    KEY `univ_cd` (`univ_cd`),\
    CONSTRAINT `capstone_design_ibfk_1` FOREIGN KEY (`univ_cd`) REFERENCES `university` (`univ_cd`)\
    ) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COMMENT='캡스톤 디자인(창의적 설계) 운영 현황';"
table_dic['캡스톤 디자인(창의적 설계) 운영 현황'] = 'capstone_design'



# 2023년_ [4-라-2. 편입학 선발 결과_]
#################################################
# 테이블명 : transfer_student | 2023년_ [4-라-2. 편입학 선발 결과_]
# 모집인원_정원내_일반편입 | 모집인원_정원내_기타 | 모집인원_정원외_학사편입 | 모집인원_정원외_특별편입학 | 모집인원_정원외_기타 | 지원자_정원내_일반편입 | 지원자_정원내_기타 | 지원자_정원외_학사편입 | 지원자_정원외_특별편입학 | 지원자_정원외_기타 | 등록인원_정원내_일반편입 | 등록인원_정원내_기타 | 등록인원_정원외_학사편입 | 
#################################################
table_dic['transfer_student'] = \
    "CREATE TABLE `transfer_student` (\
    `year` int(4) NOT NULL COMMENT '기준연도',\
    `univ_cd` varchar(10) NOT NULL COMMENT '대학 고유코드',\
    `recruitment_in_general` int(6) DEFAULT 0 COMMENT '모집인원_정원내_일반편입',\
    `recruitment_in_etc` int(6) DEFAULT 0 COMMENT '모집인원_정원내_기타',\
    `recruitment_out_bachelor` int(6) DEFAULT 0 COMMENT '모집인원_정원외_학사편입',\
    `recruitment_out_special` int(6) DEFAULT 0 COMMENT '모집인원_정원외_특별편입학',\
    `recruitment_out_etc` int(6) DEFAULT 0 COMMENT '모집인원_정원외_기타',\
    `applicant_in_general` int(6) DEFAULT 0 COMMENT '지원자_정원내_일반편입',\
    `applicant_in_etc` int(6) DEFAULT 0 COMMENT '지원자_정원내_기타',\
    `applicant_out_bachelor` int(6) DEFAULT 0 COMMENT '지원자_정원외_학사편입',\
    `applicant_out_special` int(6) DEFAULT 0 COMMENT '지원자_정원외_특별편입학',\
    `applicant_out_etc` int(6) DEFAULT 0 COMMENT '지원자_정원외_기타',\
    `registered_in_general` int(6) DEFAULT 0 COMMENT '등록인원_정원내_일반편입',\
    `registered_in_etc` int(6) DEFAULT 0 COMMENT '등록인원_정원내_기타',\
    `registered_out_bachelor` int(6) DEFAULT 0 COMMENT '등록인원_정원외_학사편입',\
    `registered_out_special` int(6) DEFAULT 0 COMMENT '등록인원_정원외_특별편입학',\
    `registered_out_etc` int(6) DEFAULT 0 COMMENT '등록인원_정원외_기타',\
    `reg_date` datetime DEFAULT CURRENT_TIMESTAMP COMMENT '생성일시',\
    `mod_date` datetime DEFAULT NULL COMMENT '수정일시',\
    PRIMARY KEY (`year`,`univ_cd`),\
    KEY `univ_cd` (`univ_cd`),\
    CONSTRAINT `transfer_student_ibfk_1` FOREIGN KEY (`univ_cd`) REFERENCES `university` (`univ_cd`)\
    ) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COMMENT='편입학 선발 결과';"
table_dic['편입학 선발 결과'] = 'transfer_student'


# 2023년_ [4-마. 재적 학생 현황_]
#################################################
# 테이블명 : enrolled_student | 2023년_ [4-마. 재적 학생 현황_]
# 학생정원 | 재학생_계_정원내 | 재학생_계_정원외 | 재학생_남_정원내 | 재학생_남_정원외 | 재학생_여_정원내 | 재학생_여_정원외 | 휴학생_계_정원내 | 휴학생_계_정원외 | 휴학생_남_정원내 | 휴학생_남_정원외 | 휴학생_여_정원내 | 휴학생_여_정원외 | 
#################################################
table_dic['enrolled_student'] = \
    "CREATE TABLE `enrolled_student` (\
    `year` int(4) NOT NULL COMMENT '기준연도',\
    `univ_cd` varchar(10) NOT NULL COMMENT '대학 고유코드',\
    `personnel_student_tot` int(6) DEFAULT 0 COMMENT '학생정원',\
    `enrolled_sum_in` int(6) DEFAULT 0 COMMENT '재학생_계_정원내',\
    `enrolled_sum_out` int(6) DEFAULT 0 COMMENT '재학생_계_정원외',\
    `enrolled_male_in` int(6) DEFAULT 0 COMMENT '재학생_남_정원내',\
    `enrolled_male_out` int(6) DEFAULT 0 COMMENT '재학생_남_정원외',\
    `enrolled_female_in` int(6) DEFAULT 0 COMMENT '재학생_여_정원내',\
    `enrolled_female_out` int(6) DEFAULT 0 COMMENT '재학생_여_정원외',\
    `absence_sum_in` int(6) DEFAULT 0 COMMENT '휴학생_계_정원내',\
    `absence_sum_out` int(6) DEFAULT 0 COMMENT '휴학생_계_정원외',\
    `absence_male_in` int(6) DEFAULT 0 COMMENT '휴학생_남_정원내',\
    `absence_male_out` int(6) DEFAULT 0 COMMENT '휴학생_남_정원외',\
    `absence_female_in` int(6) DEFAULT 0 COMMENT '휴학생_여_정원내',\
    `absence_female_out` int(6) DEFAULT 0 COMMENT '휴학생_여_정원외',\
    `suspension_sum_in` int(6) DEFAULT 0 COMMENT '학사학위취득유예학생_계_정원내',\
    `suspension_sum_out` int(6) DEFAULT 0 COMMENT '학사학위취득유예학생_계_정원외',\
    `suspension_male_in` int(6) DEFAULT 0 COMMENT '학사학위취득유예학생_남_정원내',\
    `suspension_male_out` int(7) DEFAULT 0 COMMENT '학사학위취득유예학생_남_정원외',\
    `suspension_female_in` int(8) DEFAULT 0 COMMENT '학사학위취득유예학생_여_정원내',\
    `suspension_female_out` int(9) DEFAULT 0 COMMENT '학사학위취득유예학생_여_정원외',\
    `attend_sum_in` int(10) DEFAULT 0 COMMENT '재적학생_계_정원내',\
    `attend_sum_out` int(11) DEFAULT 0 COMMENT '재적학생_계_정원외',\
    `attend_male_in` int(12) DEFAULT 0 COMMENT '재적학생_남_정원내',\
    `attend_male_out` int(13) DEFAULT 0 COMMENT '재적학생_남_정원외',\
    `attend_female_in` int(14) DEFAULT 0 COMMENT '재적학생_여_정원내',\
    `attend_female_out` int(15) DEFAULT 0 COMMENT '재적학생_여_정원외',\
    `reg_date` datetime DEFAULT CURRENT_TIMESTAMP COMMENT '생성일시',\
    `mod_date` datetime DEFAULT NULL COMMENT '수정일시',\
    PRIMARY KEY (`year`,`univ_cd`),\
    KEY `univ_cd` (`univ_cd`),\
    CONSTRAINT `enrolled_student_ibfk_1` FOREIGN KEY (`univ_cd`) REFERENCES `university` (`univ_cd`)\
    ) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COMMENT='재적 학생 현황';"
table_dic['재적 학생 현황'] = 'enrolled_student'


# 2023년_ [4-바-1. 외국학생 현황_]
#################################################
# 테이블명 : foreign_student | 2023년_ [4-바-1. 외국학생 현황_]
# 외국학생 총계 | 학위과정_소계 | 학위과정_인문사회계열 | 학위과정_자연과학계열 | 학위과정_공학계열 | 학위과정_예체능계열 | 학위과정_의학계열 | 교육과정 공동운영생 | 연수과정_소계 | 연수과정_어학연수생 | 연수과정_교환학생 | 연수과정_방문학생 | 연수과정_기타연수생 | 
#################################################
table_dic['foreign_student'] = \
    "CREATE TABLE `foreign_student` (\
    `year` int(4) NOT NULL COMMENT '기준연도',\
    `univ_cd` varchar(10) NOT NULL COMMENT '대학 고유코드',\
    `foreign_tot` int(6) DEFAULT 0 COMMENT '외국학생 총계',\
    `degree_course_sum` int(6) DEFAULT 0 COMMENT '학위과정_소계',\
    `degree_course_social_sciences` int(6) DEFAULT 0 COMMENT '학위과정_인문사회계열',\
    `degree_course_natural_science` int(6) DEFAULT 0 COMMENT '학위과정_자연과학계열',\
    `degree_course_engineering` int(6) DEFAULT 0 COMMENT '학위과정_공학계열',\
    `degree_course_arts_physical` int(6) DEFAULT 0 COMMENT '학위과정_예체능계열',\
    `degree_course_medical` int(6) DEFAULT 0 COMMENT '학위과정_의학계열',\
    `joint_operation` int(6) DEFAULT 0 COMMENT '교육과정 공동운영생',\
    `training_course_sum` int(6) DEFAULT 0 COMMENT '연수과정_소계',\
    `training_course_language` int(6) DEFAULT 0 COMMENT '연수과정_어학연수생',\
    `training_course_exchange` int(6) DEFAULT 0 COMMENT '연수과정_교환학생',\
    `training_course_visiting` int(6) DEFAULT 0 COMMENT '연수과정_방문학생',\
    `training_course_etc` int(6) DEFAULT 0 COMMENT '연수과정_기타연수생',\
    `language_skill_sum` int(6) DEFAULT 0 COMMENT '언어능력_소계',\
    `language_skill_topik4` int(6) DEFAULT 0 COMMENT '언어능력_TOPIK 4급(예체능3급)이상',\
    `language_skill_toefl530` int(6) DEFAULT 0 COMMENT '언어능력_영어트랙TOEFL 530이상',\
    `language_skill_anglosphere` int(6) DEFAULT 0 COMMENT '언어능력_영어권 외국인유학생',\
    `language_skill_rate` float(8, 2) DEFAULT 0.00 COMMENT '언어능력충족 학생비율(언어능력_소계/총계)',\
    `dormitory_degree_sum` int(6) DEFAULT 0 COMMENT '기숙사수용_학위과정_소계',\
    `dormitory_degree_accept` int(6) DEFAULT 0 COMMENT '기숙사수용_학위과정_수용',\
    `dormitory_degree_notaccept` int(6) DEFAULT 0 COMMENT '기숙사수용_학위과정_미수용',\
    `dormitory_none_degree_sum` int(6) DEFAULT 0 COMMENT '기숙사수용_비학위과정_소계',\
    `dormitory_none_degree_accept` int(6) DEFAULT 0 COMMENT '기숙사수용_비학위과정_수용',\
    `dormitory_none_degree_notaccept` int(6) DEFAULT 0 COMMENT '기숙사수용_비학위과정_미수용',\
    `reg_date` datetime DEFAULT CURRENT_TIMESTAMP COMMENT '생성일시',\
    `mod_date` datetime DEFAULT NULL COMMENT '수정일시',\
    PRIMARY KEY (`year`,`univ_cd`),\
    KEY `univ_cd` (`univ_cd`),\
    CONSTRAINT `foreign_student_ibfk_1` FOREIGN KEY (`univ_cd`) REFERENCES `university` (`univ_cd`)\
    ) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COMMENT='외국학생 현황';"
table_dic['외국학생 현황'] = 'foreign_student'



# 2023년_ [4-바-2. 외국학생 중도탈락 현황_]
#################################################
# 테이블명 : foreign_dropout_status | 2023년_ [4-바-2. 외국학생 중도탈락 현황_]
# 외국재적학생 총계 | 외국재적학생_학위과정(대학) | 외국재적학생_교육과정공동운영생 | 외국재적학생_어학연수생 | 외국재적학생_교환학생 | 외국재적학생_방문학생 | 외국재적학생_기타연수생 | 중도탈락_총계 | 중도탈락_학위과정(대학) | 중도탈락_교육과정공동운영생 | 중도탈락_어학연수생 | 중도탈락_교환학생 | 중도탈락_방문학생 | 
#################################################
table_dic['foreign_dropout_status'] = \
    "CREATE TABLE `foreign_dropout_status` (\
    `year` int(4) NOT NULL COMMENT '기준연도',\
    `univ_cd` varchar(10) NOT NULL COMMENT '대학 고유코드',\
    `foreign_tot` int(6) DEFAULT 0 COMMENT '외국재적학생 총계',\
    `foreign_degree_course` int(6) DEFAULT 0 COMMENT '외국재적학생_학위과정(대학)',\
    `foreign_joint_operation` int(6) DEFAULT 0 COMMENT '외국재적학생_교육과정공동운영생',\
    `foreign_course_language` int(6) DEFAULT 0 COMMENT '외국재적학생_어학연수생',\
    `foreign_course_exchange` int(6) DEFAULT 0 COMMENT '외국재적학생_교환학생',\
    `foreign_course_visiting` int(6) DEFAULT 0 COMMENT '외국재적학생_방문학생',\
    `foreign_etc` int(6) DEFAULT 0 COMMENT '외국재적학생_기타연수생',\
    `dropout_tot` int(6) DEFAULT 0 COMMENT '중도탈락_총계',\
    `dropout_degree_course` int(6) DEFAULT 0 COMMENT '중도탈락_학위과정(대학)',\
    `dropout_joint_operation` int(6) DEFAULT 0 COMMENT '중도탈락_교육과정공동운영생',\
    `dropout_course_language` int(6) DEFAULT 0 COMMENT '중도탈락_어학연수생',\
    `dropout_course_exchange` int(6) DEFAULT 0 COMMENT '중도탈락_교환학생',\
    `dropout_course_visiting` int(6) DEFAULT 0 COMMENT '중도탈락_방문학생',\
    `dropout_etc` int(6) DEFAULT 0 COMMENT '중도탈락_기타연수생',\
    `dropout_rate` float(8, 2) DEFAULT 0.00 COMMENT '외국학생 중도탈락율(중도탈락_총계/외국재적학생 총계)',\
    `reg_date` datetime DEFAULT CURRENT_TIMESTAMP COMMENT '생성일시',\
    `mod_date` datetime DEFAULT NULL COMMENT '수정일시',\
    PRIMARY KEY (`year`,`univ_cd`),\
    KEY `univ_cd` (`univ_cd`),\
    CONSTRAINT `foreign_dropout_status_ibfk_1` FOREIGN KEY (`univ_cd`) REFERENCES `university` (`univ_cd`)\
    ) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COMMENT='외국학생 중도탈락 현황';"
table_dic['외국학생 중도탈락 현황'] = 'foreign_dropout_status'



# 2023년_ [4-사. 중도탈락 학생 현황_]
#################################################
# 테이블명 : dropout_status | 2023년_ [4-사. 중도탈락 학생 현황_]
# 재적학생 총계 | 사유별 중도탈락_총계 | 사유별 중도탈락_미등록 | 사유별 중도탈락_미복학 | 사유별 중도탈락_자퇴 | 사유별 중도탈락_학사경고 | 사유별 중도탈락_학생활동 | 사유별 중도탈락_유급제적 | 사유별 중도탈락_재학연한초과 | 사유별 중도탈락_기타 | 중도탈락 학생 비율(사유별 중도탈락_총계/재적학생 총계) | 신입생 총계 | 신입생_사유별 중도탈락_총계 | 
#################################################
table_dic['dropout_status'] = \
    "CREATE TABLE `dropout_status` (\
    `year` int(4) NOT NULL COMMENT '기준연도',\
    `univ_cd` varchar(10) NOT NULL COMMENT '대학 고유코드',\
    `enrolled_tot` int(6) DEFAULT 0 COMMENT '재적학생 총계',\
    `dropout_case_tot` int(6) DEFAULT 0 COMMENT '사유별 중도탈락_총계',\
    `dropout_case_not_regist` int(6) DEFAULT 0 COMMENT '사유별 중도탈락_미등록',\
    `dropout_case_not_return` int(6) DEFAULT 0 COMMENT '사유별 중도탈락_미복학',\
    `dropout_case_self_dropout` int(6) DEFAULT 0 COMMENT '사유별 중도탈락_자퇴',\
    `dropout_case_academic_warning` int(6) DEFAULT 0 COMMENT '사유별 중도탈락_학사경고',\
    `dropout_case_student_activities` int(6) DEFAULT 0 COMMENT '사유별 중도탈락_학생활동',\
    `dropout_case_withdrawal` int(6) DEFAULT 0 COMMENT '사유별 중도탈락_유급제적',\
    `dropout_case_exceeded_age` int(6) DEFAULT 0 COMMENT '사유별 중도탈락_재학연한초과',\
    `dropout_case_etc` int(6) DEFAULT 0 COMMENT '사유별 중도탈락_기타',\
    `dropout_case_rate` float(8, 2) DEFAULT 0.00 COMMENT '중도탈락 학생 비율(사유별 중도탈락_총계/재적학생 총계)',\
    `fresh_tot` int(6) DEFAULT 0 COMMENT '신입생 총계',\
    `fresh_dropout_case_tot` int(6) DEFAULT 0 COMMENT '신입생_사유별 중도탈락_총계',\
    `fresh_dropout_case_not_regist` int(6) DEFAULT 0 COMMENT '신입생_사유별 중도탈락_미등록',\
    `fresh_dropout_case_not_return` int(6) DEFAULT 0 COMMENT '신입생_사유별 중도탈락_미복학',\
    `fresh_dropout_case_self_dropout` int(6) DEFAULT 0 COMMENT '신입생_사유별 중도탈락_자퇴',\
    `fresh_dropout_case_academic_warning` int(6) DEFAULT 0 COMMENT '신입생_사유별 중도탈락_학사경고',\
    `fresh_dropout_case_student_activities` int(6) DEFAULT 0 COMMENT '신입생_사유별 중도탈락_학생활동',\
    `fresh_dropout_case_withdrawal` int(6) DEFAULT 0 COMMENT '신입생_사유별 중도탈락_유급제적',\
    `fresh_dropout_case_exceeded_age` int(6) DEFAULT 0 COMMENT '신입생_사유별 중도탈락_재학연한초과',\
    `fresh_dropout_case_etc` int(6) DEFAULT 0 COMMENT '신입생_사유별 중도탈락_기타',\
    `fresh_dropout_case_rate` float(8, 2) DEFAULT 0.00 COMMENT '신입생_중도탈락 학생 비율(신입생_사유별 중도탈락 학생_총계/재적학생 총계)',\
    `reg_date` datetime DEFAULT CURRENT_TIMESTAMP COMMENT '생성일시',\
    `mod_date` datetime DEFAULT NULL COMMENT '수정일시',\
    PRIMARY KEY (`year`,`univ_cd`),\
    KEY `univ_cd` (`univ_cd`),\
    CONSTRAINT `dropout_status_ibfk_1` FOREIGN KEY (`univ_cd`) REFERENCES `university` (`univ_cd`)\
    ) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COMMENT='중도탈락 학생 현황';"
table_dic['중도탈락 학생 현황'] = 'dropout_status'




# 2023년_ [4-자. 신입생의 출신 고등학교 유형별 현황_]
#################################################
# 테이블명 : fresh_highschool_type | 2023년_ [4-자. 신입생의 출신 고등학교 유형별 현황_]
# 총입학자수 | 유형별_일반고_학생수 | 유형별_일반고_비율 | 유형별_특수목적_과학고_학생수 | 유형별_특수목적_과학고_비율 | 유형별_특수목적_외고국제고_학생수 | 유형별_특수목적_외고국제고_비율 | 유형별_특수목적_예체고_학생수 | 유형별_특수목적_예체고_비율 | 유형별_특수목적_산업수요맞춤형고_학생수 | 유형별_특수목적_산업수요맞춤형고_비율 | 유형별_특성화고_학생수 | 유형별_특성화고_비율 | 
#################################################
table_dic['fresh_highschool_type'] = \
    "CREATE TABLE `fresh_highschool_type` (\
    `year` int(4) NOT NULL COMMENT '기준연도',\
    `univ_cd` varchar(10) NOT NULL COMMENT '대학 고유코드',\
    `admission_tot` int(6) DEFAULT 0 COMMENT '총입학자수',\
    `type_general_sum` int(6) DEFAULT 0 COMMENT '유형별_일반고_학생수',\
    `type_general_rate` float(8, 2) DEFAULT 0.00 COMMENT '유형별_일반고_비율',\
    `type_special_science_sum` int(6) DEFAULT 0 COMMENT '유형별_특수목적_과학고_학생수',\
    `type_special_science_rate` float(8, 2) DEFAULT 0.00 COMMENT '유형별_특수목적_과학고_비율',\
    `type_special_foreign_sum` int(6) DEFAULT 0 COMMENT '유형별_특수목적_외고국제고_학생수',\
    `type_special_foreign_rate` float(8, 2) DEFAULT 0.00 COMMENT '유형별_특수목적_외고국제고_비율',\
    `type_special_artsports_sum` int(6) DEFAULT 0 COMMENT '유형별_특수목적_예체고_학생수',\
    `type_special_artsports_rate` float(8, 2) DEFAULT 0.00 COMMENT '유형별_특수목적_예체고_비율',\
    `type_special_industry_sum` int(6) DEFAULT 0 COMMENT '유형별_특수목적_산업수요맞춤형고_학생수',\
    `type_special_industry_rate` float(8, 2) DEFAULT 0.00 COMMENT '유형별_특수목적_산업수요맞춤형고_비율',\
    `type_specialization_sum` int(6) DEFAULT 0 COMMENT '유형별_특성화고_학생수',\
    `type_specialization_rate` float(8, 2) DEFAULT 0.00 COMMENT '유형별_특성화고_비율',\
    `type_autonomy_private_sum` int(6) DEFAULT 0 COMMENT '유형별_자율고_사립_학생수',\
    `type_autonomy_private_rate` float(8, 2) DEFAULT 0.00 COMMENT '유형별_자율고_사립_비율',\
    `type_autonomy_public_sum` int(6) DEFAULT 0 COMMENT '유형별_자율고_공립_학생수',\
    `type_autonomy_public_rate` float(8, 2) DEFAULT 0.00 COMMENT '유형별_자율고_공립_비율',\
    `type_etc_genius_sum` int(6) DEFAULT 0 COMMENT '유형별_기타_영재학교_학생수',\
    `type_etc_genius_rate` float(8, 2) DEFAULT 0.00 COMMENT '유형별_기타_영재학교_비율',\
    `type_etc_foreigner_sum` int(6) DEFAULT 0 COMMENT '유형별_기타_외국인학교_학생수',\
    `type_etc_foreigner_rate` float(8, 2) DEFAULT 0.00 COMMENT '유형별_기타_외국인학교_비율',\
    `type_etc_foreigncountry_sum` int(6) DEFAULT 0 COMMENT '유형별_기타_외국고등학교_학생수',\
    `type_etc_foreigncountry_rate` float(8, 2) DEFAULT 0.00 COMMENT '유형별_기타_외국고등학교_비율',\
    `type_etc_other_sum` int(6) DEFAULT 0 COMMENT '유형별_기타_그외기타_학생수',\
    `type_etc_other_rate` float(8, 2) DEFAULT 0.00 COMMENT '유형별_기타_그외기타_비율',\
    `type_sum` int(6) DEFAULT 0 COMMENT '유형별_소계_학생수',\
    `type_rate` float(8, 2) DEFAULT 0.00 COMMENT '유형별_소계_비율',\
    `location_specialcity_sum` int(6) DEFAULT 0 COMMENT '지역별_특별시_학생수',\
    `location_specialcity_rate` float(8, 2) DEFAULT 0.00 COMMENT '지역별_특별시_비율',\
    `location_metropolitan_sum` int(6) DEFAULT 0 COMMENT '지역별_광역시,특별자치시_학생수',\
    `location_metropolitan_rate` float(8, 2) DEFAULT 0.00 COMMENT '지역별_광역시,특별자치시_비율',\
    `location_medium_sum` int(6) DEFAULT 0 COMMENT '지역별_중소도시_학생수',\
    `location_medium_rate` float(8, 2) DEFAULT 0.00 COMMENT '지역별_중소도시_비율',\
    `location_small_sum` int(6) DEFAULT 0 COMMENT '지역별_읍면_학생수',\
    `location_small_rate` float(8, 2) DEFAULT 0.00 COMMENT '지역별_읍면_비율',\
    `location_special_sum` int(6) DEFAULT 0 COMMENT '지역별_특수_학생수',\
    `location_special_rate` float(8, 2) DEFAULT 0.00 COMMENT '지역별_특수_비율',\
    `location_etc_sum` int(6) DEFAULT 0 COMMENT '지역별_기타_학생수',\
    `location_etc_rate` float(8, 2) DEFAULT 0.00 COMMENT '지역별_기타_비율',\
    `location_sum` int(6) DEFAULT 0 COMMENT '지역별_소계_학생수',\
    `location_rate` float(8, 2) DEFAULT 0.00 COMMENT '지역별_소계_비율',\
    `reg_date` datetime DEFAULT CURRENT_TIMESTAMP COMMENT '생성일시',\
    `mod_date` datetime DEFAULT NULL COMMENT '수정일시',\
    PRIMARY KEY (`year`,`univ_cd`),\
    KEY `univ_cd` (`univ_cd`),\
    CONSTRAINT `fresh_highschool_type_ibfk_1` FOREIGN KEY (`univ_cd`) REFERENCES `university` (`univ_cd`)\
    ) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COMMENT='신입생의 출신 고등학교 유형별 현황';"
table_dic['신입생의 출신 고등학교 유형별 현황'] = 'fresh_highschool_type'






# # XXXX
# #################################################
# # 테이블명 : XXXXX | XXXXX
# # 필드 : year    | DEL      | DEL     | DEL  | DEL | DEL   | completed_stud_dept | completed_stud_human_social | completed_stud_natural_science | completed_stud_engineering | completed_stud_medicine | support_amount_stud_tot | support_amount_prototype | support_amount_education |
# # 설명 : 기준연도 | 학교종류 | 설립구분 | 지역 | 상태 | 학교명 | 이수학생수_해당학과 | 이수학생수_타학과_인문사회 | 이수학생수_타학과_자연과학 | 이수학생수_타학과_공학 | 이수학생수_타학과_의학 | 이수학생수_타학과_예체능 | 지원금수령_학생수(명) | 지원금수령_금액_시제품제작비 | 지원금수령_금액_교육프로그램지원비
# #################################################
# table_dic['XXXX'] = \
#     "CREATE TABLE `XXXXX` (\
#     `year` int(4) NOT NULL COMMENT '기준연도',\
#     `univ_cd` varchar(10) NOT NULL COMMENT '대학 고유코드',\
#     `` int(6) DEFAULT 0 COMMENT '',\
#     `` int(6) DEFAULT 0 COMMENT '',\
#     `` int(6) DEFAULT 0 COMMENT '',\
#     `` int(6) DEFAULT 0 COMMENT '',\
#     `` int(6) DEFAULT 0 COMMENT '',\
        

#     PRIMARY KEY (`year`,`univ_cd`),\
#     KEY `univ_cd` (`univ_cd`),\
#     CONSTRAINT `XXXXX_ibfk_1` FOREIGN KEY (`univ_cd`) REFERENCES `university` (`univ_cd`)\
#     ) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COMMENT='XXXX';"
# table_dic['XXXXX'] = 'XXXXX'



# 2023년_ [4-다. 신입생 충원 현황_] 테이블
#################################################
# 테이블명 : new_students | 신입생 충원 현황
# 필드 : year    | DEL      | DEL     | DEL  | DEL | DEL | admission_tot |  recruit_tot | recruit_in      | recruit_out     | applicant_tot | applicant_in  | applicant_out | admitted_tot | admitted_in_m | admitted_in_f   | admitted_out_m   | admitted_out_f   | recruit_rate       | competition_rate
# 설명 : 기준연도 | 학교종류 | 설립구분 | 지역 | 상태 | 학교 | 입학정원      | 모집인원(계) | 모집인원(정원내)  | 모집인원(정원외) | 지원자(계)     | 지원자(정원내) | 지원자(정원외) | 입학자(계) | 입학자(정원내)-남 | 입학자(정원내)-녀 | 입학자(정원외)-남 | 입학자(정원외)-녀 | 정원내 신입생 충원율 | 경쟁률
#################################################
table_dic['new_students'] = \
    "CREATE TABLE `new_students` (\
    `year` int(4) NOT NULL COMMENT '기준연도',\
    `univ_cd` varchar(10) NOT NULL COMMENT '대학 고유코드',\
    `admission_tot` int(6) DEFAULT 0 COMMENT '입학정원',\
    `recruit_tot` int(6) DEFAULT 0 COMMENT '모집인원(계)',\
    `recruit_in` int(6) DEFAULT 0 COMMENT '모집인원(정원내)',\
    `recruit_out` int(6) DEFAULT 0 COMMENT '모집인원(정원외)',\
    `applicant_tot` int(6) DEFAULT 0 COMMENT '지원자(계)',\
    `applicant_in` int(6) DEFAULT 0 COMMENT '지원자(정원내)',\
    `applicant_out` int(6) DEFAULT 0 COMMENT '지원자(정원외)',\
    `admitted_tot` int(6) DEFAULT 0 COMMENT '입학자(계)',\
    `admitted_in_m` int(6) DEFAULT 0 COMMENT '입학자(정원내)-남',\
    `admitted_in_f` int(6) DEFAULT 0 COMMENT '입학자(정원내)-녀',\
    `admitted_out_m` int(6) DEFAULT 0 COMMENT '입학자(정원외)-남',\
    `admitted_out_f` int(6) DEFAULT 0 COMMENT '입학자(정원외)-녀',\
    `recruit_rate` float(8, 2) DEFAULT 0.00 COMMENT '정원내 신입생 충원율[입학자(정원내)/모집인원(정원내)]',\
    `competition_rate` float(8, 2) DEFAULT 0.00 COMMENT '경쟁률[지원자(정원내)/모집인원(정원내)]',\
    `reg_date` datetime DEFAULT CURRENT_TIMESTAMP COMMENT '생성일시',\
    `mod_date` datetime DEFAULT NULL COMMENT '수정일시',\
    PRIMARY KEY (`year`,`univ_cd`),\
    KEY `univ_cd` (`univ_cd`),\
    CONSTRAINT `new_students_ibfk_1` FOREIGN KEY (`univ_cd`) REFERENCES `university` (`univ_cd`)\
    ) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COMMENT='신입생 충원 현황';"
table_dic['신입생 충원 현황'] = 'new_students'



############################################################### 재학생 충원율은 기준년도가 상반기, 하반기...... ##############

# 2023년_ [4-라-1. 재학생 충원율_]
#################################################
# 테이블명 : student_recruitment_rate | 2023년_ [4-라-1. 재학생 충원율_]
# 학생정원 | 학생모집정지인원 | 재학생_계 | 재학생_정원내 | 재학생_정원외 | 재학생 충원율 | 재학생 충원율_정원내 |  |  |  |  |  |  | 
#################################################
table_dic['student_recruitment_rate'] = \
    "CREATE TABLE `student_recruitment_rate` (\
    `year` varchar(200) COMMENT '기준연도',\
    `univ_cd` varchar(10) NOT NULL COMMENT '대학 고유코드',\
    `personnel_student_tot` int(6) DEFAULT 0 COMMENT '학생정원', \
    `recruitment_suspension_sum` int(6) DEFAULT 0 COMMENT '학생모집정지인원', \
    `students_tot` int(6) DEFAULT 0 COMMENT '재학생_계', \
    `students_in` int(6) DEFAULT 0 COMMENT '재학생_정원내', \
    `students_out` int(6) DEFAULT 0 COMMENT '재학생_정원외', \
    `students_recruitment_rate` float(8, 2) DEFAULT 0.00 COMMENT '재학생 충원율', \
    `students_recruitment_rate_in` float(8, 2) DEFAULT 0.00 COMMENT '재학생 충원율_정원내', \
    PRIMARY KEY (`year`,`univ_cd`),\
    KEY `univ_cd` (`univ_cd`),\
    CONSTRAINT `student_recruitment_rate_ibfk_1` FOREIGN KEY (`univ_cd`) REFERENCES `university` (`univ_cd`)\
    ) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COMMENT='재학생 충원율';"
table_dic['재학생 충원율'] = 'student_recruitment_rate'



# # 2023년_ [3-나. 전임 입학사정관 현황_]
# #################################################
# # 테이블명 : admissions_officer | 전임 입학사정관 현황
# # 필드 : year    | DEL      | DEL     | DEL  | DEL | DEL   | completed_stud_dept | completed_stud_human_social | completed_stud_natural_science | completed_stud_engineering | completed_stud_medicine | support_amount_stud_tot | support_amount_prototype | support_amount_education |
# # 설명 : 기준연도 | 학교종류 | 설립구분 | 지역 | 상태 | 학교명 | 이수학생수_해당학과 | 이수학생수_타학과_인문사회 | 이수학생수_타학과_자연과학 | 이수학생수_타학과_공학 | 이수학생수_타학과_의학 | 이수학생수_타학과_예체능 | 지원금수령_학생수(명) | 지원금수령_금액_시제품제작비 | 지원금수령_금액_교육프로그램지원비
# #################################################
# table_dic['admissions_officer'] = \
#     "CREATE TABLE `admissions_officer` (\
#     `year` int(4) NOT NULL COMMENT '기준연도',\
#     `univ_cd` varchar(10) NOT NULL COMMENT '대학 고유코드',\
#     `employ_office_tot` int(6) DEFAULT 0 COMMENT '채용사정관_총인원',\
#     `employ_office_ft_tot` int(6) DEFAULT 0 COMMENT '채용사정관_정규직인원',\
#     `employ_office_ft_rate` float(8, 2) DEFAULT 0.00 COMMENT '채용사정관_정규직비율',\
#     `professor_office_tot` int(6) DEFAULT 0 COMMENT '교수사정관_총인원',\
#     `professor_office_ft_tot` int(6) DEFAULT 0 COMMENT '교수사정관_정규직인원',\
#     `professor_office_ft_rate` float(8, 2) DEFAULT 0.00 COMMENT '교수사정관_정규직비율',\
#     `transition_office_tot` int(6) DEFAULT 0 COMMENT '전환사정관_총인원',\
#     `transition_office_ft_tot` int(6) DEFAULT 0 COMMENT '전환사정관_정규직인원',\
#     `transition_office_ft_rate` float(8, 2) DEFAULT 0.00 COMMENT '전환사정관_정규직비율',\
#     `sub_office_tot` int(6) DEFAULT 0 COMMENT '소계_사정관 총인원',\
#     `sub_office_ft_tot` int(6) DEFAULT 0 COMMENT '소계_사정관_정규직인원',\
#     `sub_office_ft_rate` float(8, 2) DEFAULT 0.00 COMMENT '소계_사정관 정규직비율',\
#     `appointment_tot` int(6) DEFAULT 0 COMMENT '위촉사정관_총인원',\
#     `total_tot` int(6) DEFAULT 0 COMMENT '총계_총인원',\
#     `reg_date` datetime DEFAULT CURRENT_TIMESTAMP COMMENT '생성일시',\
#     `mod_date` datetime DEFAULT NULL COMMENT '수정일시',\
#     PRIMARY KEY (`year`,`univ_cd`),\
#     KEY `univ_cd` (`univ_cd`),\
#     CONSTRAINT `admissions_officer_ibfk_1` FOREIGN KEY (`univ_cd`) REFERENCES `university` (`univ_cd`)\
#     ) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COMMENT='전임 입학사정관 현황';"
# table_dic['전임 입학사정관 현황'] = 'admissions_officer'



# # 2023년_ [3-다. 학교생활기록부의 기록과 자기소개서 등 교과성적 외의 자료를 활용하는 입학전형에서 서류평가를 담당한 평가자 1명당 서류평가 건수_]
# #################################################
# # 테이블명 : admission_officer_number | 2023년_ [3-다. 학교생활기록부의 기록과 자기소개서 등 교과성적 외의 자료를 활용하는 입학전형에서 서류평가를 담당한 평가자 1명당 서류평가 건수_]
# # 서류평가 참여 입학사정관 인원_전임사정관 | 서류평가 참여 입학사정관 인원_위촉사정관 | 서류평가 참여 입학사정관 인원_전체사정관 | 모집인원 | 서류평가대상인원 | 서류평가 건수_전임사정관 | 서류평가 건수_위촉사정관 | 서류평가 건수_전체사정관 | 입학사정관 1명당 서류평가 건수_전임사정관 | 입학사정관 1명당 서류평가 건수_위촉사정관 | 입학사정관 1명당 서류평가 건수_전체사정관 |  |  | 
# #################################################
# table_dic['admission_officer_number'] = \
#     "CREATE TABLE `admission_officer_number` (\
#     `year` int(4) NOT NULL COMMENT '기준연도',\
#     `univ_cd` varchar(10) NOT NULL COMMENT '대학 고유코드',\
#     `admission_officer_fulltime` int(6) DEFAULT 0 COMMENT '서류평가 참여 입학사정관 인원_전임사정관', \
#     `admission_officer_appointment` int(6) DEFAULT 0 COMMENT '서류평가 참여 입학사정관 인원_위촉사정관', \
#     `admission_officer_tot` int(6) DEFAULT 0 COMMENT '서류평가 참여 입학사정관 인원_전체사정관', \
#     `recruitment_tot` int(6) DEFAULT 0 COMMENT '모집인원', \
#     `target_stud_tot` int(6) DEFAULT 0 COMMENT '서류평가대상인원', \
#     `evaluation_num_fulltime` int(6) DEFAULT 0 COMMENT '서류평가 건수_전임사정관', \
#     `evaluation_num_appointment` int(6) DEFAULT 0 COMMENT '서류평가 건수_위촉사정관', \
#     `evaluation_num_tot` int(6) DEFAULT 0 COMMENT '서류평가 건수_전체사정관', \
#     `num_per_officer_fulltime` int(6) DEFAULT 0 COMMENT '입학사정관 1명당 서류평가 건수_전임사정관', \
#     `num_per_officer_appointment` int(6) DEFAULT 0 COMMENT '입학사정관 1명당 서류평가 건수_위촉사정관', \
#     `num_per_officer_tot` int(6) DEFAULT 0 COMMENT '입학사정관 1명당 서류평가 건수_전체사정관', \
#     PRIMARY KEY (`year`,`univ_cd`),\
#     KEY `univ_cd` (`univ_cd`),\
#     CONSTRAINT `admission_officer_number_ibfk_1` FOREIGN KEY (`univ_cd`) REFERENCES `university` (`univ_cd`)\
#     ) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COMMENT='학교생활기록부의 기록과 자기소개서 등 교과성적 외의 자료를 활용하는 입학전형에서 서류평가를 담당한 평가자 1명당 서류평가 건수';"
# table_dic['학교생활기록부의 기록과 자기소개서 등 교과성적 외의 자료를 활용하는 입학전형에서 서류평가를 담당한 평가자 1명당 서류평가 건수'] = 'admission_officer_number'





#################################################################################################################################################
#
# 인덱스 생성 후 숫자로 키값을 정하는 케이스
# 학교명 등 셀이 통합되어있음.....
#################################################################################################################################################

# 2023년_ [12-카-4-(1). 계약학과 설치 운영 현황_]
#################################################
# 테이블명 : contract_department | 계약학과 설치 운영 현황
# 필드 : year    | DEL      | DEL     | DEL  | DEL | DEL  | degree  | contract_department_type | department | parent_department | parent_department_tot | contract_department_name | courses_classification_type | contract_department_tot | fresh_stud_tot | enrolled_stud_tot | area    | use_external_learning  | contract_type 
#                                                        | expense_industry_rate    | expense_agency_rate        | expense_univ_rate      | expense_stud_rate     | expense_support_agency | expense_support_title | recruitment_graduate | recruitment_employed_contract  | recruitment_employed_other_industry | industry_tot
# 설명 : 기준연도 | 학교종류 | 설립구분 | 지역 | 상태 | 학교 | 취득학위 | 계약학과 유형             | 계열        | 모체학과 명칭 | 모체학과 입학정원           | 계약학과 명칭             | 신/편입과정 구분             | 계약학과 정원            | 입학생 수       | 재학생수           | 설치권역 | 외부학습장 이용여부     | 계약형태  
#                                                        | 경비부담_산업체경비_부담률 | 경비부담_외부기관경비_지원율 | 경비부담_대학자체_감면율 | 경비부담_학생경비_부담률 | 경비지원_기관명         | 경비지원_사업명        | 채용조건형_졸업자      | 채용조건형_취업자_계약산업체     | 채용조건형_취업자_타산업체    | 산업체수
#################################################

table_dic['contract_department'] = \
    "CREATE TABLE `contract_department` (\
    `idx` int auto_increment NOT NULL COMMENT '고유키 인덱스',\
    `year` int(4) NOT NULL COMMENT '기준연도',\
    `univ_cd` varchar(10) NOT NULL COMMENT '대학 고유코드',\
    `degree` varchar(200) COMMENT '취득학위',\
    `contract_department_type` varchar(200) COMMENT '계약학과 유형',\
    `department` varchar(200) COMMENT '계열',\
    `parent_department` varchar(200) COMMENT '모체학과 명칭',\
    `parent_department_tot` int(6) DEFAULT 0 COMMENT '모체학과 입학정원',\
    `contract_department_name` varchar(200) COMMENT '계약학과 명칭',\
    `courses_classification_type` varchar(200) COMMENT '신/편입과정 구분',\
    `contract_department_tot` int(6) DEFAULT 0 COMMENT '계약학과 정원',\
    `fresh_stud_tot` int(6) DEFAULT 0 COMMENT '입학생 수',\
    `enrolled_stud_tot` int(6) DEFAULT 0 COMMENT '재학생수',\
    `area` varchar(200) COMMENT '설치권역',\
    `use_external_learning` varchar(200) COMMENT '외부학습장 이용여부',\
    `contract_type` varchar(200) COMMENT '계약형태',\
    `expense_industry_rate` float(8, 2) DEFAULT 0.00 COMMENT '경비부담_산업체경비_부담률',\
    `expense_agency_rate` float(8, 2) DEFAULT 0.00 COMMENT '경비부담_외부기관경비_지원율',\
    `expense_univ_rate` float(8, 2) DEFAULT 0.00 COMMENT '경비부담_대학자체_감면율',\
    `expense_stud_rate` float(8, 2) DEFAULT 0.00 COMMENT '경비부담_학생경비_부담률',\
    `expense_support_agency` varchar(200) COMMENT '경비지원_기관명',\
    `expense_support_title` varchar(200) COMMENT '경비지원_사업명',\
    `recruitment_graduate` varchar(200) COMMENT '채용조건형_졸업자',\
    `recruitment_employed_contract` varchar(200) COMMENT '채용조건형_취업자_계약산업체',\
    `recruitment_employed_other_industry` varchar(200) COMMENT '채용조건형_취업자_타산업체',\
    `industry_tot` int(6) DEFAULT 0 COMMENT '산업체수',\
    `reg_date` datetime DEFAULT CURRENT_TIMESTAMP COMMENT '생성일시',\
    `mod_date` datetime DEFAULT NULL COMMENT '수정일시',\
    PRIMARY KEY (`idx`),\
    KEY `univ_cd` (`univ_cd`),\
    CONSTRAINT `contract_department_ibfk_1` FOREIGN KEY (`univ_cd`) REFERENCES `university` (`univ_cd`)\
    ) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COMMENT='계약학과 설치 운영 현황';"
table_dic['계약학과 설치 운영 현황'] = 'contract_department'



# 2023년 _대학_4-가. 입학전형 유형별 선발 결과_학교별자료
#################################################
# 테이블명 : admission_result_type | 2023년 _대학_4-가. 입학전형 유형별 선발 결과_학교별자료
# 고유키 인덱스 | 정원구분 | 전형유형 | 전형명(대분류) | 전형명(중분류) | 전형명(소분류) | 수시_모집인원 | 수시_등록인원 | 수시_등록률 | 정시_모집인원 | 정시_등록인원 | 정시_등록률 | 추가_모집인원 | 
#################################################
table_dic['admission_result_type'] = \
    "CREATE TABLE `admission_result_type` (\
    `idx` int(11) NOT NULL AUTO_INCREMENT COMMENT '고유키 인덱스', \
    `year` int(4) NOT NULL COMMENT '기준연도',\
    `univ_cd` varchar(10) NOT NULL COMMENT '대학 고유코드',\
    `recruitment_type` varchar(200) COMMENT '정원구분',\
    `process_type` varchar(200) COMMENT '전형유형',\
    `process_name_1` varchar(200) COMMENT '전형명(대분류)',\
    `process_name_2` varchar(200) COMMENT '전형명(중분류)',\
    `process_name_3` varchar(200) COMMENT '전형명(소분류)',\
    `occasion_recruitment` int(6) DEFAULT 0 COMMENT '수시_모집인원', \
    `occasion_registered` int(6) DEFAULT 0 COMMENT '수시_등록인원', \
    `occasion_regist_rate` float(8, 2) DEFAULT 0.00 COMMENT '수시_등록률', \
    `ontime_recruitment` int(6) DEFAULT 0 COMMENT '정시_모집인원', \
    `ontime_registered` int(6) DEFAULT 0 COMMENT '정시_등록인원', \
    `ontime_regist_rate` float(8, 2) DEFAULT 0.00 COMMENT '정시_등록률', \
    `addition_recruitment` int(6) DEFAULT 0 COMMENT '추가_모집인원', \
    `addition_registered` int(6) DEFAULT 0 COMMENT '추가_등록인원', \
    `addition_regist_rate` float(8, 2) DEFAULT 0.00 COMMENT '추가_등록률', \
    `final_recruitment` int(6) DEFAULT 0 COMMENT '최종_모집인원', \
    `final_registered` int(6) DEFAULT 0 COMMENT '최종_등록인원', \
    `final_regist_rate` float(8, 2) DEFAULT 0.00 COMMENT '최종_등록률', \
    `reg_date` datetime DEFAULT CURRENT_TIMESTAMP COMMENT '생성일시',\
    `mod_date` datetime DEFAULT NULL COMMENT '수정일시',\
    PRIMARY KEY (`idx`),\
    KEY `univ_cd` (`univ_cd`),\
    CONSTRAINT `admission_result_type_ibfk_1` FOREIGN KEY (`univ_cd`) REFERENCES `university` (`univ_cd`)\
    ) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COMMENT='입학전형 유형별 선발 결과';"
table_dic['입학전형 유형별 선발 결과'] = 'admission_result_type'



# 2023년_ [12-카-4-(2). 주문식 교육과정 설치 운영 현황_]
#################################################
# 테이블명 : ondemand_curriculum | 2023년_ [12-카-4-(2). 주문식 교육과정 설치 운영 현황_]
# 고유키 인덱스 | 학위과정 | 계열 | 주문식 교육과정명 | 운영유형 | 채용유형 | 참여학과 | 참여학생수 | 약정인원 | 산업체수 | 주문식교육과정 졸업자 | 취업자_약정 산업체 | 취업자_타 산업체 | 
#################################################
table_dic['ondemand_curriculum'] = \
    "CREATE TABLE `ondemand_curriculum` (\
    `idx` int(11) NOT NULL AUTO_INCREMENT COMMENT '고유키 인덱스', \
    `year` int(4) NOT NULL COMMENT '기준연도',\
    `univ_cd` varchar(10) NOT NULL COMMENT '대학 고유코드',\
    `degree_course` varchar(200) COMMENT '학위과정',\
    `department` varchar(200) COMMENT '계열',\
    `ondemand_curriculum_name` varchar(200) COMMENT '주문식 교육과정명',\
    `operate_type` varchar(200) COMMENT '운영유형',\
    `employment_type` varchar(200) COMMENT '채용유형',\
    `participation_department` varchar(200) COMMENT '참여학과',\
    `participation_stud_sum` int(6) DEFAULT 0 COMMENT '참여학생수', \
    `agreement_sum` int(6) DEFAULT 0 COMMENT '약정인원', \
    `industry_sum` int(6) DEFAULT 0 COMMENT '산업체수', \
    `ondemand_curriculum_graduate` int(6) DEFAULT 0 COMMENT '주문식교육과정 졸업자', \
    `employed_agreement_industry` int(6) DEFAULT 0 COMMENT '취업자_약정 산업체', \
    `employed_other_industry` int(6) DEFAULT 0 COMMENT '취업자_타 산업체', \
    `tuition_industry_rate` float(8, 2) DEFAULT 0.00 COMMENT '등록금부담 현황_산업체 부담률', \
    `tuition_external_rate` float(8, 2) DEFAULT 0.00 COMMENT '등록금부담 현황_외부기관 지원율', \
    `tuition_university_rate` float(8, 2) DEFAULT 0.00 COMMENT '등록금부담 현황_대학 자체 감면율', \
    `tuition_student_rate` float(8, 2) DEFAULT 0.00 COMMENT '등록금부담 현황_학생 등록금 부담률', \
    `expense_support_agency` varchar(200) COMMENT '경비지원 외부기관_기관명',\
    `expense_support_title` varchar(200) COMMENT '경비지원 외부기관_사업명',\
    `reg_date` datetime DEFAULT CURRENT_TIMESTAMP COMMENT '생성일시',\
    `mod_date` datetime DEFAULT NULL COMMENT '수정일시',\
    PRIMARY KEY (`idx`),\
    KEY `univ_cd` (`univ_cd`),\
    CONSTRAINT `ondemand_curriculum_ibfk_1` FOREIGN KEY (`univ_cd`) REFERENCES `university` (`univ_cd`)\
    ) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COMMENT='주문식 교육과정 설치 운영 현황';"
table_dic['주문식 교육과정 설치 운영 현황'] = 'ondemand_curriculum'









#####################################################################################################################################################################################################################################################
##################################################################################################################################################################################################################################################### 
# 2. 교육 여건
#####################################################################################################################################################################################################################################################
#####################################################################################################################################################################################################################################################



# 2023년_ [3-나. 전임 입학사정관 현황_]
#################################################
# 테이블명 : admissions_officer | 2023년_ [3-나. 전임 입학사정관 현황_]
# 채용사정관_총인원 | 채용사정관_정규직인원 | 채용사정관_정규직비율 | 교수사정관_총인원 | 교수사정관_정규직인원 | 교수사정관_정규직비율 | 전환사정관_총인원 | 전환사정관_정규직인원 | 전환사정관_정규직비율 | 소계_사정관 총인원 | 소계_사정관_정규직인원 | 소계_사정관 정규직비율 | 위촉사정관_총인원 | 
#################################################
table_dic['admissions_officer'] = \
    "CREATE TABLE `admissions_officer` (\
    `year` int(4) NOT NULL COMMENT '기준연도',\
    `univ_cd` varchar(10) NOT NULL COMMENT '대학 고유코드',\
    `employ_office_tot` int(6) DEFAULT 0 COMMENT '채용사정관_총인원', \
    `employ_office_ft_tot` int(6) DEFAULT 0 COMMENT '채용사정관_정규직인원', \
    `employ_office_ft_rate` float(8, 2) DEFAULT 0.00 COMMENT '채용사정관_정규직비율', \
    `professor_office_tot` int(6) DEFAULT 0 COMMENT '교수사정관_총인원', \
    `professor_office_ft_tot` int(6) DEFAULT 0 COMMENT '교수사정관_정규직인원', \
    `professor_office_ft_rate` float(8, 2) DEFAULT 0.00 COMMENT '교수사정관_정규직비율', \
    `transition_office_tot` int(6) DEFAULT 0 COMMENT '전환사정관_총인원', \
    `transition_office_ft_tot` int(6) DEFAULT 0 COMMENT '전환사정관_정규직인원', \
    `transition_office_ft_rate` float(8, 2) DEFAULT 0.00 COMMENT '전환사정관_정규직비율', \
    `sub_office_tot` int(6) DEFAULT 0 COMMENT '소계_사정관 총인원', \
    `sub_office_ft_tot` int(6) DEFAULT 0 COMMENT '소계_사정관_정규직인원', \
    `sub_office_ft_rate` float(8, 2) DEFAULT 0.00 COMMENT '소계_사정관 정규직비율', \
    `appointment_tot` int(6) DEFAULT 0 COMMENT '위촉사정관_총인원', \
    `total_tot` int(6) DEFAULT 0 COMMENT '총계_총인원', \
    `reg_date` datetime DEFAULT CURRENT_TIMESTAMP COMMENT '생성일시',\
    `mod_date` datetime DEFAULT NULL COMMENT '수정일시',\
    PRIMARY KEY (`year`,`univ_cd`),\
    KEY `univ_cd` (`univ_cd`),\
    CONSTRAINT `admissions_officer_ibfk_1` FOREIGN KEY (`univ_cd`) REFERENCES `university` (`univ_cd`)\
    ) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COMMENT='전임 입학사정관 현황';"
table_dic['전임 입학사정관 현황'] = 'admissions_officer'


# 2023년_ [3-다. 학교생활기록부의 기록과 자기소개서 등 교과성적 외의 자료를 활용하는 입학전형에서 서류평가를 담당한 평가자 1명당 서류평가 건수_]
#################################################
# 테이블명 : admission_officer_number | 2023년_ [3-다. 학교생활기록부의 기록과 자기소개서 등 교과성적 외의 자료를 활용하는 입학전형에서 서류평가를 담당한 평가자 1명당 서류평가 건수_]
# 서류평가 참여 입학사정관 인원_전임사정관 | 서류평가 참여 입학사정관 인원_위촉사정관 | 서류평가 참여 입학사정관 인원_전체사정관 | 모집인원 | 서류평가대상인원 | 서류평가 건수_전임사정관 | 서류평가 건수_위촉사정관 | 서류평가 건수_전체사정관 | 입학사정관 1명당 서류평가 건수_전임사정관 | 입학사정관 1명당 서류평가 건수_위촉사정관 | 입학사정관 1명당 서류평가 건수_전체사정관 |  |  | 
#################################################
table_dic['admission_officer_number'] = \
    "CREATE TABLE `admission_officer_number` (\
    `year` int(4) NOT NULL COMMENT '기준연도',\
    `univ_cd` varchar(10) NOT NULL COMMENT '대학 고유코드',\
    `admission_officer_fulltime` int(6) DEFAULT 0 COMMENT '서류평가 참여 입학사정관 인원_전임사정관', \
    `admission_officer_appointment` int(6) DEFAULT 0 COMMENT '서류평가 참여 입학사정관 인원_위촉사정관', \
    `admission_officer_tot` int(6) DEFAULT 0 COMMENT '서류평가 참여 입학사정관 인원_전체사정관', \
    `recruitment_tot` int(6) DEFAULT 0 COMMENT '모집인원', \
    `target_stud_tot` int(6) DEFAULT 0 COMMENT '서류평가대상인원', \
    `evaluation_num_fulltime` int(6) DEFAULT 0 COMMENT '서류평가 건수_전임사정관', \
    `evaluation_num_appointment` int(6) DEFAULT 0 COMMENT '서류평가 건수_위촉사정관', \
    `evaluation_num_tot` int(6) DEFAULT 0 COMMENT '서류평가 건수_전체사정관', \
    `num_per_officer_fulltime` int(6) DEFAULT 0 COMMENT '입학사정관 1명당 서류평가 건수_전임사정관', \
    `num_per_officer_appointment` int(6) DEFAULT 0 COMMENT '입학사정관 1명당 서류평가 건수_위촉사정관', \
    `num_per_officer_tot` int(6) DEFAULT 0 COMMENT '입학사정관 1명당 서류평가 건수_전체사정관', \
    `reg_date` datetime DEFAULT CURRENT_TIMESTAMP COMMENT '생성일시',\
    `mod_date` datetime DEFAULT NULL COMMENT '수정일시',\
    PRIMARY KEY (`year`,`univ_cd`),\
    KEY `univ_cd` (`univ_cd`),\
    CONSTRAINT `admission_officer_number_ibfk_1` FOREIGN KEY (`univ_cd`) REFERENCES `university` (`univ_cd`)\
    ) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COMMENT='학교생활기록부의 기록과 자기소개서 등 교과성적 외의 자료를 활용하는 입학전형에서 서류평가를 담당한 평가자 1명당 서류평가 건수';"
table_dic['학교생활기록부의 기록과 자기소개서 등 교과성적 외의 자료를 활용하는 입학전형에서 서류평가를 담당한 평가자 1명당 서류평가 건수'] = 'admission_officer_number'


# 2023년_ [6-가-1. 전체 교원 대비 전임교원 현황_]
#################################################
# 테이블명 : fulltime_professor_status | 2023년_ [6-가-1. 전체 교원 대비 전임교원 현황_]
# 전체합계_남 | 전체합계_여 | 학부_전임교원_계_남 | 학부_전임교원_계_여 | 학부_전임교원_교수_남 | 학부_전임교원_교수_여 | 학부_전임교원_부교수_남 | 학부_전임교원_부교수_여 | 학부_전임교원_조교수_남 | 학부_전임교원_조교수_여 | 학부_비전임교원_계_남 | 학부_비전임교원_계_여 | 학부_비전임교원_겸임_남 | 
#################################################
table_dic['fulltime_professor_status'] = \
    "CREATE TABLE `fulltime_professor_status` (\
    `year` int(4) NOT NULL COMMENT '기준연도',\
    `univ_cd` varchar(10) NOT NULL COMMENT '대학 고유코드',\
    `tot_male` int(6) DEFAULT 0 COMMENT '전체합계_남', \
    `tot_female` int(6) DEFAULT 0 COMMENT '전체합계_여', \
    `undergraduate_fulltime_tot_male` int(6) DEFAULT 0 COMMENT '학부_전임교원_계_남', \
    `undergraduate_fulltime_tot_female` int(6) DEFAULT 0 COMMENT '학부_전임교원_계_여', \
    `undergraduate_fulltime_professor_male` int(6) DEFAULT 0 COMMENT '학부_전임교원_교수_남', \
    `undergraduate_fulltime_professor_female` int(6) DEFAULT 0 COMMENT '학부_전임교원_교수_여', \
    `undergraduate_fulltime_associate_male` int(6) DEFAULT 0 COMMENT '학부_전임교원_부교수_남', \
    `undergraduate_fulltime_associate_female` int(6) DEFAULT 0 COMMENT '학부_전임교원_부교수_여', \
    `undergraduate_fulltime_assistant_male` int(6) DEFAULT 0 COMMENT '학부_전임교원_조교수_남', \
    `undergraduate_fulltime_assistant_female` int(6) DEFAULT 0 COMMENT '학부_전임교원_조교수_여', \
    `undergraduate_parttime_tot_male` int(6) DEFAULT 0 COMMENT '학부_비전임교원_계_남', \
    `undergraduate_parttime_tot_female` int(6) DEFAULT 0 COMMENT '학부_비전임교원_계_여', \
    `undergraduate_parttime_concurrent_male` int(6) DEFAULT 0 COMMENT '학부_비전임교원_겸임_남', \
    `undergraduate_parttime_concurrent_female` int(6) DEFAULT 0 COMMENT '학부_비전임교원_겸임_여', \
    `undergraduate_parttime_invite_male` int(6) DEFAULT 0 COMMENT '학부_비전임교원_초빙_남', \
    `undergraduate_parttime_invite_female` int(6) DEFAULT 0 COMMENT '학부_비전임교원_초빙_여', \
    `undergraduate_parttime_time_male` int(6) DEFAULT 0 COMMENT '학부_비전임교원_시간강사_남', \
    `undergraduate_parttime_time_female` int(6) DEFAULT 0 COMMENT '학부_비전임교원_시간강사_여', \
    `undergraduate_parttime_instructor_male` int(6) DEFAULT 0 COMMENT '학부_비전임교원_강사_남', \
    `undergraduate_parttime_instructor_female` int(6) DEFAULT 0 COMMENT '학부_비전임교원_강사_여', \
    `undergraduate_parttime_etc_male` int(6) DEFAULT 0 COMMENT '학부_비전임교원_기타_남', \
    `undergraduate_parttime_etc_female` int(6) DEFAULT 0 COMMENT '학부_비전임교원_기타_여', \
    `graduate_fulltime_tot_male` int(6) DEFAULT 0 COMMENT '대학원_전임교원_계_남', \
    `graduate_fulltime_tot_female` int(6) DEFAULT 0 COMMENT '대학원_전임교원_계_여', \
    `graduate_fulltime_professor_male` int(6) DEFAULT 0 COMMENT '대학원_전임교원_교수_남', \
    `graduate_fulltime_professor_female` int(6) DEFAULT 0 COMMENT '대학원_전임교원_교수_여', \
    `graduate_fulltime_associate_male` int(6) DEFAULT 0 COMMENT '대학원_전임교원_부교수_남', \
    `graduate_fulltime_associate_female` int(6) DEFAULT 0 COMMENT '대학원_전임교원_부교수_여', \
    `graduate_fulltime_assistant_male` int(6) DEFAULT 0 COMMENT '대학원_전임교원_조교수_남', \
    `graduate_fulltime_assistant_female` int(6) DEFAULT 0 COMMENT '대학원_전임교원_조교수_여', \
    `graduate_parttime_tot_male` int(6) DEFAULT 0 COMMENT '대학원_비전임교원_계_남', \
    `graduate_parttime_tot_female` int(6) DEFAULT 0 COMMENT '대학원_비전임교원_계_여', \
    `graduate_parttime_concurrent_male` int(6) DEFAULT 0 COMMENT '대학원_비전임교원_겸임_남', \
    `graduate_parttime_concurrent_female` int(6) DEFAULT 0 COMMENT '대학원_비전임교원_겸임_여', \
    `graduate_parttime_invite_male` int(6) DEFAULT 0 COMMENT '대학원_비전임교원_초빙_남', \
    `graduate_parttime_invite_female` int(6) DEFAULT 0 COMMENT '대학원_비전임교원_초빙_여', \
    `graduate_parttime_time_male` int(6) DEFAULT 0 COMMENT '대학원_비전임교원_시간강사_남', \
    `graduate_parttime_time_female` int(6) DEFAULT 0 COMMENT '대학원_비전임교원_시간강사_여', \
    `graduate_parttime_instructor_male` int(6) DEFAULT 0 COMMENT '대학원_비전임교원_강사_남', \
    `graduate_parttime_instructor_female` int(6) DEFAULT 0 COMMENT '대학원_비전임교원_강사_여', \
    `graduate_parttime_etc_male` int(6) DEFAULT 0 COMMENT '대학원_비전임교원_기타_남', \
    `graduate_parttime_etc_female` int(6) DEFAULT 0 COMMENT '대학원_비전임교원_기타_여', \
    `reg_date` datetime DEFAULT CURRENT_TIMESTAMP COMMENT '생성일시',\
    `mod_date` datetime DEFAULT NULL COMMENT '수정일시',\
    PRIMARY KEY (`year`,`univ_cd`),\
    KEY `univ_cd` (`univ_cd`),\
    CONSTRAINT `fulltime_professor_status_ibfk_1` FOREIGN KEY (`univ_cd`) REFERENCES `university` (`univ_cd`)\
    ) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COMMENT='전체 교원 대비 전임교원 현황';"
table_dic['전체 교원 대비 전임교원 현황'] = 'fulltime_professor_status'




# 2023년_ [6-가-2. 전체 신규 전임교원 현황_]
#################################################
# 테이블명 : new_fulltime_professor_status | 2023년_ [6-가-2. 전체 신규 전임교원 현황_]
# 기준일자 | 신규전임교원_합계_남 | 신규전임교원_합계_여 | 신규전임교원_교수_남 | 신규전임교원_교수_여 | 신규전임교원_부교수_남 | 신규전임교원_부교수_여 | 신규전임교원_조교수_남 | 신규전임교원_조교수_여 |  |  |  |  | 
#################################################
table_dic['new_fulltime_professor_status'] = \
    "CREATE TABLE `new_fulltime_professor_status` (\
    `year` int(4) NOT NULL COMMENT '기준연도',\
    `univ_cd` varchar(10) NOT NULL COMMENT '대학 고유코드',\
    `reference_date` varchar(200) COMMENT '기준일자',\
    `new_fulltime_tot_male` int(6) DEFAULT 0 COMMENT '신규전임교원_합계_남', \
    `new_fulltime_tot_female` int(6) DEFAULT 0 COMMENT '신규전임교원_합계_여', \
    `new_fulltime_professor_male` int(6) DEFAULT 0 COMMENT '신규전임교원_교수_남', \
    `new_fulltime_professor_female` int(6) DEFAULT 0 COMMENT '신규전임교원_교수_여', \
    `new_fulltime_associate_male` int(6) DEFAULT 0 COMMENT '신규전임교원_부교수_남', \
    `new_fulltime_associate_female` int(6) DEFAULT 0 COMMENT '신규전임교원_부교수_여', \
    `new_fulltime_assistant_male` int(6) DEFAULT 0 COMMENT '신규전임교원_조교수_남', \
    `new_fulltime_assistant_female` int(6) DEFAULT 0 COMMENT '신규전임교원_조교수_여', \
    `reg_date` datetime DEFAULT CURRENT_TIMESTAMP COMMENT '생성일시',\
    `mod_date` datetime DEFAULT NULL COMMENT '수정일시',\
    PRIMARY KEY (`year`,`univ_cd`),\
    KEY `univ_cd` (`univ_cd`),\
    CONSTRAINT `new_fulltime_professor_status_ibfk_1` FOREIGN KEY (`univ_cd`) REFERENCES `university` (`univ_cd`)\
    ) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COMMENT='전체 신규 전임교원 현황';"
table_dic['전체 신규 전임교원 현황'] = 'new_fulltime_professor_status'




# 2023년_ [6-나-(1). 전임교원 1인당 학생 수 및 전임교원 확보율_]
#################################################
# 테이블명 : professor_acquisition_rate_per_student | 2023년_ [6-나-(1). 전임교원 1인당 학생 수 및 전임교원 확보율_]
# 학생현황_학부_학생정원 | 학생현황_학부_재학생 | 학생현황_대학원_학생정원 | 학생현황_대학원_재학생 | 학생현황_학생정원_계(A1) | 학생현황_재학생_계(A2) | 전임교원현황_학생정원기준 전임교원(B1) | 전임교원현황_재학생기준 전임교원(B2) | 교원 법정정원_학생정원기준_계(C1) | 교원 법정정원_재학생기준_계(C2) | 전임교원1인당 학생수_학생정원기준(A1/B1) | 전임교원1인당 학생수_재학생기준(A2/B2) | 전임교원 확보율_학생정원기준(B1/C1*100) | 
#################################################
table_dic['professor_acquisition_rate_per_student'] = \
    "CREATE TABLE `professor_acquisition_rate_per_student` (\
    `year` int(4) NOT NULL COMMENT '기준연도',\
    `univ_cd` varchar(10) NOT NULL COMMENT '대학 고유코드',\
    `stud_undergraduate_capacity_sum` int(6) DEFAULT 0 COMMENT '학생현황_학부_학생정원', \
    `stud_undergraduate_enrolled_sum` int(6) DEFAULT 0 COMMENT '학생현황_학부_재학생', \
    `stud_graduate_capacity_sum` int(6) DEFAULT 0 COMMENT '학생현황_대학원_학생정원', \
    `stud_graduate_enrolled_sum` int(6) DEFAULT 0 COMMENT '학생현황_대학원_재학생', \
    `stud_capacity_tot` int(6) DEFAULT 0 COMMENT '학생현황_학생정원_계(A1)', \
    `stud_enrolled_tot` int(6) DEFAULT 0 COMMENT '학생현황_재학생_계(A2)', \
    `fulltime_capacity_criteria` int(6) DEFAULT 0 COMMENT '전임교원현황_학생정원기준 전임교원(B1)', \
    `fulltime_enrolled_criteria` int(6) DEFAULT 0 COMMENT '전임교원현황_재학생기준 전임교원(B2)', \
    `legal_quota_capacity_criteria_sum` int(6) DEFAULT 0 COMMENT '교원 법정정원_학생정원기준_계(C1)', \
    `legal_quota_enrolled_criteria_sum` int(6) DEFAULT 0 COMMENT '교원 법정정원_재학생기준_계(C2)', \
    `stud_per_fulltime_capacity_criteria_sum` float(8, 2) DEFAULT 0.00 COMMENT '전임교원1인당 학생수_학생정원기준(A1/B1)', \
    `stud_per_fulltime_enrolled_criteria_sum` float(8, 2) DEFAULT 0.00 COMMENT '전임교원1인당 학생수_재학생기준(A2/B2)', \
    `fulltime_acquisition_capacity_criteria_rate` float(8, 2) DEFAULT 0.00 COMMENT '전임교원 확보율_학생정원기준(B1/C1*100)', \
    `fulltime_acquisition_enrolled_criteria_rate` float(8, 2) DEFAULT 0.00 COMMENT '전임교원 확보율_재학생기준(B2/C2*100)', \
    `reg_date` datetime DEFAULT CURRENT_TIMESTAMP COMMENT '생성일시',\
    `mod_date` datetime DEFAULT NULL COMMENT '수정일시',\
    PRIMARY KEY (`year`,`univ_cd`),\
    KEY `univ_cd` (`univ_cd`),\
    CONSTRAINT `professor_acquisition_rate_per_student_ibfk_1` FOREIGN KEY (`univ_cd`) REFERENCES `university` (`univ_cd`)\
    ) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COMMENT='전임교원 1인당 학생 수 및 전임교원 확보율';"
table_dic['전임교원 1인당 학생 수 및 전임교원 확보율'] = 'professor_acquisition_rate_per_student'





# 2023년_ [12-거. 기술지주회사 운영 현황_]
#################################################
# 테이블명 : tech_holding_company_status | 2023년_ [12-거. 기술지주회사 운영 현황_]
# 기술지주회사(또는 신기술창업전문회사)_상호명 | 기술지주회사(또는 신기술창업전문회사)_설립일자 | 기술지주회사(또는 신기술창업전문회사)_지주회사 자본금_총액(원) | 기술지주회사(또는 신기술창업전문회사)_지주회사 자본금_현금(원) | 기술지주회사(또는 신기술창업전문회사)_지주회사 자본금_현물(원) | 산학협력단 출자액(원) | 지주회사 매출액_총 매출액(원) | 지주회사 매출액_지분매각수익(원) | 지주회사 매출액_배당수익(원) | 지주회사 고용인력(명) | 자회사_수 | 자회사_총 고용인력 | 자회사_자본금 총액 | 
#################################################
table_dic['tech_holding_company_status'] = \
    "CREATE TABLE `tech_holding_company_status` (\
    `year` int(4) NOT NULL COMMENT '기준연도',\
    `univ_cd` varchar(10) NOT NULL COMMENT '대학 고유코드',\
    `tech_holding_title` varchar(200) COMMENT '기술지주회사(또는 신기술창업전문회사)_상호명',\
    `tech_holding_establish` varchar(200) COMMENT '기술지주회사(또는 신기술창업전문회사)_설립일자',\
    `tech_holding_capital_tot` int(11) DEFAULT 0 COMMENT '기술지주회사(또는 신기술창업전문회사)_지주회사 자본금_총액(원)', \
    `tech_holding_capital_cash` int(11) DEFAULT 0 COMMENT '기술지주회사(또는 신기술창업전문회사)_지주회사 자본금_현금(원)', \
    `tech_holding_capital_goods` int(11) DEFAULT 0 COMMENT '기술지주회사(또는 신기술창업전문회사)_지주회사 자본금_현물(원)', \
    `industry_collaboration_contribution` int(11) DEFAULT 0 COMMENT '산학협력단 출자액(원)', \
    `holding_revenue_tot` int(11) DEFAULT 0 COMMENT '지주회사 매출액_총 매출액(원)', \
    `holding_revenue_equity_disposal` int(11) DEFAULT 0 COMMENT '지주회사 매출액_지분매각수익(원)', \
    `holding_revenue_dividend_income` int(11) DEFAULT 0 COMMENT '지주회사 매출액_배당수익(원)', \
    `holding_employment` int(6) DEFAULT 0 COMMENT '지주회사 고용인력(명)', \
    `subsidiary_num` int(6) DEFAULT 0 COMMENT '자회사_수', \
    `subsidiary_employment_tot` int(6) DEFAULT 0 COMMENT '자회사_총 고용인력', \
    `subsidiary_capital_tot` int(11) DEFAULT 0 COMMENT '자회사_자본금 총액', \
    `subsidiary_revenue_tot` int(11) DEFAULT 0 COMMENT '자회사_총 매출액(원)', \
    `location` varchar(200) COMMENT '입지현황',\
     `reg_date` datetime DEFAULT CURRENT_TIMESTAMP COMMENT '생성일시',\
    `mod_date` datetime DEFAULT NULL COMMENT '수정일시',\
    PRIMARY KEY (`year`,`univ_cd`),\
    KEY `univ_cd` (`univ_cd`),\
    CONSTRAINT `tech_holding_company_status_ibfk_1` FOREIGN KEY (`univ_cd`) REFERENCES `university` (`univ_cd`)\
    ) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COMMENT='기술지주회사 운영 현황';"
table_dic['기술지주회사 운영 현황'] = 'tech_holding_company_status'



# 2023년_ [12-나-3. 대학 강의 공개 현황_]
#################################################
# 테이블명 : open_lecture_status | 2023년_ [12-나-3. 대학 강의 공개 현황_]
# 한국형 온라인공개 강좌(K-MOOC) 강좌 수 | KOCW_강의 동영상 공개 강좌 수 | KOCW_멀티미디어 자료 공개 강좌 수 | KOCW_강의자료 공개 강좌 수 | KOCW_전체 공개 건수(주차) |  |  |  |  |  |  |  |  | 
#################################################
table_dic['open_lecture_status'] = \
    "CREATE TABLE `open_lecture_status` (\
    `year` int(4) NOT NULL COMMENT '기준연도',\
    `univ_cd` varchar(10) NOT NULL COMMENT '대학 고유코드',\
    `kmooc_tot` int(6) DEFAULT 0 COMMENT '한국형 온라인공개 강좌(K-MOOC) 강좌 수', \
    `kocw_online_sum` int(6) DEFAULT 0 COMMENT 'KOCW_강의 동영상 공개 강좌 수', \
    `kocw_multimedia_sum` int(6) DEFAULT 0 COMMENT 'KOCW_멀티미디어 자료 공개 강좌 수', \
    `kocw_lecture_data_sum` int(6) DEFAULT 0 COMMENT 'KOCW_강의자료 공개 강좌 수', \
    `kocw_open_tot_week` int(6) DEFAULT 0 COMMENT 'KOCW_전체 공개 건수(주차)', \
    `reg_date` datetime DEFAULT CURRENT_TIMESTAMP COMMENT '생성일시',\
    `mod_date` datetime DEFAULT NULL COMMENT '수정일시',\
    PRIMARY KEY (`year`,`univ_cd`),\
    KEY `univ_cd` (`univ_cd`),\
    CONSTRAINT `open_lecture_status_ibfk_1` FOREIGN KEY (`univ_cd`) REFERENCES `university` (`univ_cd`)\
    ) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COMMENT='대학 강의 공개 현황';"
table_dic['대학 강의 공개 현황'] = 'open_lecture_status'




# 2023년_ [12-아. 산업체 경력 전임교원 현황_]
#################################################
# 테이블명 : industrial_experience_professor | 2023년_ [12-아. 산업체 경력 전임교원 현황_]
# 5년 이내 신규임용 전임교원_경력 없음 | 5년 이내 신규임용 전임교원_산업체경력 전임교원_1년 미만 | 5년 이내 신규임용 전임교원_산업체경력 전임교원_1년~3년 미만 | 5년 이내 신규임용 전임교원_산업체경력 전임교원_3년~5년 미만 | 5년 이내 신규임용 전임교원_산업체경력 전임교원_5년~10년 미만 | 5년 이내 신규임용 전임교원_산업체경력 전임교원_10년 이상 | 산학협력 중점교수_채용형 전임 | 산학협력 중점교수_지정형 전임 | 산학협력 중점교수_비전임 |  |  |  |  | 
#################################################
table_dic['industrial_experience_professor'] = \
    "CREATE TABLE `industrial_experience_professor` (\
    `year` int(4) NOT NULL COMMENT '기준연도',\
    `univ_cd` varchar(10) NOT NULL COMMENT '대학 고유코드',\
    `new_fulltime_experience_no` int(5) DEFAULT 0 COMMENT '5년 이내 신규임용 전임교원_경력 없음', \
    `new_fulltime_experience_0_1_year` int(5) DEFAULT 0 COMMENT '5년 이내 신규임용 전임교원_산업체경력 전임교원_1년 미만', \
    `new_fulltime_experience_1_3_year` int(5) DEFAULT 0 COMMENT '5년 이내 신규임용 전임교원_산업체경력 전임교원_1년~3년 미만', \
    `new_fulltime_experience_3_5_year` int(5) DEFAULT 0 COMMENT '5년 이내 신규임용 전임교원_산업체경력 전임교원_3년~5년 미만', \
    `new_fulltime_experience_5_10_year` int(5) DEFAULT 0 COMMENT '5년 이내 신규임용 전임교원_산업체경력 전임교원_5년~10년 미만', \
    `new_fulltime_experience_10_up_year` int(5) DEFAULT 0 COMMENT '5년 이내 신규임용 전임교원_산업체경력 전임교원_10년 이상', \
    `industry_collaboration_fulltime_employment` int(5) DEFAULT 0 COMMENT '산학협력 중점교수_채용형 전임', \
    `industry_collaboration_fulltime_designated` int(5) DEFAULT 0 COMMENT '산학협력 중점교수_지정형 전임', \
    `industry_collaboration_parttime` int(5) DEFAULT 0 COMMENT '산학협력 중점교수_비전임', \
    `reg_date` datetime DEFAULT CURRENT_TIMESTAMP COMMENT '생성일시',\
    `mod_date` datetime DEFAULT NULL COMMENT '수정일시',\
    PRIMARY KEY (`year`,`univ_cd`),\
    KEY `univ_cd` (`univ_cd`),\
    CONSTRAINT `industrial_experience_professor_ibfk_1` FOREIGN KEY (`univ_cd`) REFERENCES `university` (`univ_cd`)\
    ) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COMMENT='산업체 경력 전임교원 현황';"
table_dic['산업체 경력 전임교원 현황'] = 'industrial_experience_professor'


# 2023년_ [13-가. 장서 보유 및 도서관 예산 현황_]
#################################################
# 테이블명 : books_and_library_budget | 2023년_ [13-가. 장서 보유 및 도서관 예산 현황_]
# 재학생 수(A) | 도서자료_계(B) | 도서자료_국내(책) | 도서자료_국외(책) | 연간 도서자료 증가 책수_증가(책) | 연간 도서자료 증가 책수_폐기(책) | 비도서 자료(종) | 전자자료_계 | 전자자료_국내(패키지) | 전자자료_국외(패키지) | 인쇄형 연속간행물_계 | 인쇄형 연속간행물_국내(종) | 인쇄형 연속간행물_국외(종) | 
#################################################
table_dic['books_and_library_budget'] = \
    "CREATE TABLE `books_and_library_budget` (\
    `year` int(4) NOT NULL COMMENT '기준연도',\
    `univ_cd` varchar(10) NOT NULL COMMENT '대학 고유코드',\
    `enrolled_student_tot` int(6) DEFAULT 0 COMMENT '재학생 수(A)', \
    `book_tot` int(11) DEFAULT 0 COMMENT '도서자료_계(B)', \
    `book_domestic` int(11) DEFAULT 0 COMMENT '도서자료_국내(책)', \
    `book_oversea` int(11) DEFAULT 0 COMMENT '도서자료_국외(책)', \
    `book_increase_year` int(11) DEFAULT 0 COMMENT '연간 도서자료 증가 책수_증가(책)', \
    `book_dispose_year` int(11) DEFAULT 0 COMMENT '연간 도서자료 증가 책수_폐기(책)', \
    `none_book` int(11) DEFAULT 0 COMMENT '비도서 자료(종)', \
    `electronic_tot` int(11) DEFAULT 0 COMMENT '전자자료_계', \
    `electronic_domestic` int(11) DEFAULT 0 COMMENT '전자자료_국내(패키지)', \
    `electronic_oversea` int(11) DEFAULT 0 COMMENT '전자자료_국외(패키지)', \
    `print_publication_tot` int(11) DEFAULT 0 COMMENT '인쇄형 연속간행물_계', \
    `print_publication_domestic` int(11) DEFAULT 0 COMMENT '인쇄형 연속간행물_국내(종)', \
    `print_publication_oversea` int(11) DEFAULT 0 COMMENT '인쇄형 연속간행물_국외(종)', \
    `settlement_tot` int(14) DEFAULT 0 COMMENT '대학 총결산(C)', \
    `purchase_cost` int(11) DEFAULT 0 COMMENT '자료 구입비(D)', \
    `book_per_student` float(8, 2) DEFAULT 0.00 COMMENT '학생 1인당 도서자료 수(B/A)', \
    `purchase_cost_rate` float(8, 2) DEFAULT 0.00 COMMENT '대학 총결산 대비 자료구입비 비율', \
    `purchase_cost_per_student` float(8, 2) DEFAULT 0.00 COMMENT '학생 1인당 자료 구입비(D/A)', \
    `reg_date` datetime DEFAULT CURRENT_TIMESTAMP COMMENT '생성일시',\
    `mod_date` datetime DEFAULT NULL COMMENT '수정일시',\
    PRIMARY KEY (`year`,`univ_cd`),\
    KEY `univ_cd` (`univ_cd`),\
    CONSTRAINT `books_and_library_budget_ibfk_1` FOREIGN KEY (`univ_cd`) REFERENCES `university` (`univ_cd`)\
    ) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COMMENT='장서 보유 및 도서관 예산 현황';"
table_dic['장서 보유 및 도서관 예산 현황'] = 'books_and_library_budget'


# 2023년_ [14-다. 교지(校地) 확보 현황_]
#################################################
# 테이블명 : area_acquisition_status | 2023년_ [14-다. 교지(校地) 확보 현황_]
# 기준면적(㎡)_입학정원 기준(A) | 기준면적(㎡)_재학생 기준(A) | 보유면적(㎡)(C) | 교지확보율(%)_입학정원 기준(C/A*100) | 교지확보율(%)_재학생 기준(C/B *100) |  |  |  |  |  |  |  |  | 
#################################################
table_dic['area_acquisition_status'] = \
    "CREATE TABLE `area_acquisition_status` (\
    `year` int(4) NOT NULL COMMENT '기준연도',\
    `univ_cd` varchar(10) NOT NULL COMMENT '대학 고유코드',\
    `area_tot` bigint(20) DEFAULT 0 COMMENT '토지 전체면적(㎡)'\
    `area_acquisition` bigint(20) DEFAULT 0 COMMENT '교지 보유면적(㎡)'\
    `area_sub` bigint(20) DEFAULT 0 COMMENT '부속토지(㎡)'\
    `area_unused` bigint(20) DEFAULT 0 COMMENT '미사용토지(㎡)'\
    `area_admission_capacity` int(8) DEFAULT 0 COMMENT '기준면적(㎡)_입학정원 기준(A)',\
    `area_enrolled_student` int(8) DEFAULT 0 COMMENT '기준면적(㎡)_재학생 기준(A)', \
    `acquisition_area` int(8) DEFAULT 0 COMMENT '보유면적(㎡)(C)', \
    `acquisition_admission_rate` float(8, 2) DEFAULT 0.00 COMMENT '교지확보율(%)_입학정원 기준(C/A*100)', \
    `acquisition_enrolled_rate` float(8, 2) DEFAULT 0.00 COMMENT '교지확보율(%)_재학생 기준(C/B *100)', \
    `reg_date` datetime DEFAULT CURRENT_TIMESTAMP COMMENT '생성일시',\
    `mod_date` datetime DEFAULT NULL COMMENT '수정일시',\
    PRIMARY KEY (`year`,`univ_cd`),\
    KEY `univ_cd` (`univ_cd`),\
    CONSTRAINT `area_acquisition_status_ibfk_1` FOREIGN KEY (`univ_cd`) REFERENCES `university` (`univ_cd`)\
    ) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COMMENT='교지(校地) 확보 현황';"
table_dic['교지(校地) 확보 현황'] = 'area_acquisition_status'

# 24년 부터로 구조가 많이 바뀜
# ALTER TABLE swu_external.area_acquisition_status ADD area_sub bigint(20) DEFAULT 0 NULL COMMENT '부속토지(㎡)';
# ALTER TABLE swu_external.area_acquisition_status CHANGE area_sub area_sub bigint(20) DEFAULT 0 NULL COMMENT '부속토지(㎡)' AFTER area_acquisition;
# ALTER TABLE swu_external.area_acquisition_status ADD area_unused bigint(20) DEFAULT 0 NULL COMMENT '미사용토지(㎡)';
# ALTER TABLE swu_external.area_acquisition_status CHANGE area_unused area_unused bigint(20) DEFAULT 0 NULL COMMENT '미사용토지(㎡)' AFTER area_sub;
# ALTER TABLE swu_external.area_acquisition_status CHANGE area_tot area_tot bigint(20) DEFAULT 0 NULL COMMENT '토지 전체면적(㎡)' AFTER univ_cd;
# ALTER TABLE swu_external.area_acquisition_status ADD area_tot bigint(20) DEFAULT 0 NULL COMMENT '토지 전체면적(㎡)';
# ALTER TABLE swu_external.area_acquisition_status CHANGE area_acquisition area_acquisition bigint(20) DEFAULT 0 NULL COMMENT '교지 보유면적(㎡)' AFTER area_tot;
# ALTER TABLE swu_external.area_acquisition_status ADD area_acquisition bigint(20) DEFAULT 0 NULL COMMENT '교지 보유면적(㎡)';





# 2023년_ [14-마-2-(1). 기숙사 운영 결과(국·공립_민자)_]
#################################################
# 테이블명 : dormitory_result_national_univ_capital | 2023년_ [14-마-2-(1). 기숙사 운영 결과(국·공립_민자)_]
# 수익_지원금수입_국고 | 수익_지원금수입_학교 | 수익_기숙사비 수익 | 수익_부속시설 초과수익 | 수익_기타수익 | 수익_소계(A) | 비용_시설 임차료 | 비용_인건비 | 비용_운영비_운영 관리비 | 비용_운영비_수선 유지비 | 비용_운영비_협약 외 운영비 | 비용_학생경비 | 비용_기타비용 | 
#################################################
table_dic['dormitory_result_national_univ_capital'] = \
    "CREATE TABLE `dormitory_result_national_univ_capital` (\
    `year` int(4) NOT NULL COMMENT '기준연도',\
    `univ_cd` varchar(10) NOT NULL COMMENT '대학 고유코드',\
    `revenue_support_exchequer` bigint(20) COMMENT '수익_지원금수입_국고',\
    `revenue_support_university` bigint(20) COMMENT '수익_지원금수입_학교',\
    `revenue_dormitory` bigint(20) COMMENT '수익_기숙사비 수익',\
    `revenue_attached` bigint(20) COMMENT '수익_부속시설 초과수익',\
    `revenue_etc` bigint(20) COMMENT '수익_기타수익',\
    `revenue_sum` bigint(20) COMMENT '수익_소계(A)',\
    `expense_facility_rental` bigint(20) COMMENT '비용_시설 임차료',\
    `expense_personnel` bigint(20) COMMENT '비용_인건비',\
    `expense_operation_management` bigint(20) COMMENT '비용_운영비_운영 관리비',\
    `expense_operation_repair` bigint(20) COMMENT '비용_운영비_수선 유지비',\
    `expense_operation_etc` bigint(20) COMMENT '비용_운영비_협약 외 운영비',\
    `expense_student` bigint(20) COMMENT '비용_학생경비',\
    `expense_etc` bigint(20) COMMENT '비용_기타비용',\
    `expense_sum` bigint(20) COMMENT '비용_소계(B)',\
    `remark` varchar(500) COMMENT '비고',\
    `reg_date` datetime DEFAULT CURRENT_TIMESTAMP COMMENT '생성일시',\
    `mod_date` datetime DEFAULT NULL COMMENT '수정일시',\
    PRIMARY KEY (`year`,`univ_cd`),\
    KEY `univ_cd` (`univ_cd`),\
    CONSTRAINT `dormitory_result_national_univ_capital_ibfk_1` FOREIGN KEY (`univ_cd`) REFERENCES `university` (`univ_cd`)\
    ) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COMMENT='기숙사 운영 결과(국·공립_민자)';"
table_dic['기숙사 운영 결과(국·공립_민자)'] = 'dormitory_result_national_univ_capital'







# 2023년_ [14-마-2-(3). 기숙사 운영 결과(국·공립_직영)_]
#################################################
# 테이블명 : dormitory_result_national_univ_direct | 2023년_ [14-마-2-(3). 기숙사 운영 결과(국·공립_직영)_]
# 수익_기숙사비 수익 | 수익_임대료 수익 | 수익_기타 수익 | 수익_소계(A) | 비용_인건비 | 비용_위탁관리비 | 비용_공공요금 및 제세 | 비용_수선비 | 비용_감가상각비 | 비용_일반수용비 | 비용_학생경비 | 비용_기타 | 비용_소계(B) | 
#################################################
table_dic['dormitory_result_national_univ_direct'] = \
    "CREATE TABLE `dormitory_result_national_univ_direct` (\
    `year` int(4) NOT NULL COMMENT '기준연도',\
    `univ_cd` varchar(10) NOT NULL COMMENT '대학 고유코드',\
    `revenue_dormitory` bigint(20) COMMENT '수익_기숙사비 수익',\
    `revenue_rental` bigint(20) COMMENT '수익_임대료 수익',\
    `revenue_etc` bigint(20) COMMENT '수익_기타 수익',\
    `revenue_sum` bigint(20) COMMENT '수익_소계(A)',\
    `expense_personnel` bigint(20) COMMENT '비용_인건비',\
    `expense_consignment` bigint(20) COMMENT '비용_위탁관리비',\
    `expense_utility` bigint(20) COMMENT '비용_공공요금 및 제세',\
    `expense_repair` bigint(20) COMMENT '비용_수선비',\
    `expense_depreciation` bigint(20) COMMENT '비용_감가상각비',\
    `expense_accommodation` bigint(20) COMMENT '비용_일반수용비',\
    `expense_student` bigint(20) COMMENT '비용_학생경비',\
    `expense_etc` bigint(20) COMMENT '비용_기타',\
    `expense_sum` bigint(20) COMMENT '비용_소계(B)',\
    `remark` varchar(500) COMMENT '비고',\
    `reg_date` datetime DEFAULT CURRENT_TIMESTAMP COMMENT '생성일시',\
    `mod_date` datetime DEFAULT NULL COMMENT '수정일시',\
    PRIMARY KEY (`year`,`univ_cd`),\
    KEY `univ_cd` (`univ_cd`),\
    CONSTRAINT `dormitory_result_national_univ_direct_ibfk_1` FOREIGN KEY (`univ_cd`) REFERENCES `university` (`univ_cd`)\
    ) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COMMENT='기숙사 운영 결과(국·공립_직영)';"
table_dic['기숙사 운영 결과(국·공립_직영)'] = 'dormitory_result_national_univ_direct'




# 2023년_ [14-마-2-(4). 기숙사 운영 결과(사립_직영)_]
#################################################
# 테이블명 : dormitory_result_private_univ_direct | 2023년_ [14-마-2-(4). 기숙사 운영 결과(사립_직영)_]
# 수익_기숙사비 수익 | 수익_임대료 수익 | 수익_기타 수익 | 수익_소계(A) | 비용_인건비 | 비용_위탁관리비 | 비용_공공요금 및 제세 | 비용_수선비 | 비용_감가상각비 | 비용_일반수용비 | 비용_학생경비 | 비용_기타 | 비용_소계(B) | 
#################################################
table_dic['dormitory_result_private_univ_direct'] = \
    "CREATE TABLE `dormitory_result_private_univ_direct` (\
    `year` int(4) NOT NULL COMMENT '기준연도',\
    `univ_cd` varchar(10) NOT NULL COMMENT '대학 고유코드',\
    `revenue_dormitory` bigint(20) COMMENT '수익_기숙사비 수익',\
    `revenue_rental` bigint(20) COMMENT '수익_임대료 수익',\
    `revenue_etc` bigint(20) COMMENT '수익_기타 수익',\
    `revenue_sum` bigint(20) COMMENT '수익_소계(A)',\
    `expense_personnel` bigint(20) COMMENT '비용_인건비',\
    `expense_consignment` bigint(20) COMMENT '비용_위탁관리비',\
    `expense_utility` bigint(20) COMMENT '비용_공공요금 및 제세',\
    `expense_repair` bigint(20) COMMENT '비용_수선비',\
    `expense_depreciation` bigint(20) COMMENT '비용_감가상각비',\
    `expense_accommodation` bigint(20) COMMENT '비용_일반수용비',\
    `expense_student` bigint(20) COMMENT '비용_학생경비',\
    `expense_etc` bigint(20) COMMENT '비용_기타',\
    `expense_sum` bigint(20) COMMENT '비용_소계(B)',\
    `remark` varchar(500) COMMENT '비고',\
    `reg_date` datetime DEFAULT CURRENT_TIMESTAMP COMMENT '생성일시',\
    `mod_date` datetime DEFAULT NULL COMMENT '수정일시',\
    PRIMARY KEY (`year`,`univ_cd`),\
    KEY `univ_cd` (`univ_cd`),\
    CONSTRAINT `dormitory_result_private_univ_direct_ibfk_1` FOREIGN KEY (`univ_cd`) REFERENCES `university` (`univ_cd`)\
    ) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COMMENT='기숙사 운영 결과(사립_직영)';"
table_dic['기숙사 운영 결과(사립_직영)'] = 'dormitory_result_private_univ_direct'






#####################################################################################################################################################################################################################################################
##################################################################################################################################################################################################################################################### 
# 3. 교육 연구 성과
#####################################################################################################################################################################################################################################################
#####################################################################################################################################################################################################################################################

# 2023년_ [5-다. 졸업생의 취업 현황_]
#################################################
# 테이블명 : graduate_employment_status | 2023년_ [5-다. 졸업생의 취업 현황_]
# 졸업자_남 | 졸업자_여 | 취업자_건강보험 직장가입자_남 | 취업자_건강보험 직장가입자_여 | 취업자_해외_남 | 취업자_해외_여 | 취업자_농림어업 종사_남 | 취업자_농림어업 종사_여 | 취업자_개인 창작활동 종사_남 | 취업자_개인 창작활동 종사_여 | 취업자_1인 창(사)업_남 | 취업자_1인 창(사)업_여 | 취업자_프리랜서_남 | 
#################################################
table_dic['graduate_employment_status'] = \
    "CREATE TABLE `graduate_employment_status` (\
    `year` int(4) NOT NULL COMMENT '기준연도',\
    `univ_cd` varchar(10) NOT NULL COMMENT '대학 고유코드',\
    `graduate_male` int(6) DEFAULT 0 COMMENT '졸업자_남', \
    `graduate_female` int(6) DEFAULT 0 COMMENT '졸업자_여', \
    `employed_insurance_male` int(6) DEFAULT 0 COMMENT '취업자_건강보험 직장가입자_남', \
    `employed_insurance_female` int(6) DEFAULT 0 COMMENT '취업자_건강보험 직장가입자_여', \
    `employed_oversea_male` int(6) DEFAULT 0 COMMENT '취업자_해외_남', \
    `employed_oversea_female` int(6) DEFAULT 0 COMMENT '취업자_해외_여', \
    `employed_agriculture_male` int(6) DEFAULT 0 COMMENT '취업자_농림어업 종사_남', \
    `employed_agriculture_female` int(6) DEFAULT 0 COMMENT '취업자_농림어업 종사_여', \
    `employed_creative_male` int(6) DEFAULT 0 COMMENT '취업자_개인 창작활동 종사_남', \
    `employed_creative_female` int(6) DEFAULT 0 COMMENT '취업자_개인 창작활동 종사_여', \
    `employed_solo_proprietor_male` int(6) DEFAULT 0 COMMENT '취업자_1인 창(사)업_남', \
    `employed_solo_proprietor_female` int(6) DEFAULT 0 COMMENT '취업자_1인 창(사)업_여', \
    `employed_freelancer_male` int(6) DEFAULT 0 COMMENT '취업자_프리랜서_남', \
    `employed_freelancer_female` int(6) DEFAULT 0 COMMENT '취업자_프리랜서_여', \
    `enrolled_male` int(6) DEFAULT 0 COMMENT '진학자(C)_남', \
    `enrolled_female` int(6) DEFAULT 0 COMMENT '진학자(C)_여', \
    `army` int(6) DEFAULT 0 COMMENT '입대자(D)', \
    `unemployable_male` int(6) DEFAULT 0 COMMENT '취업불가능자(E)_남', \
    `unemployable_female` int(6) DEFAULT 0 COMMENT '취업불가능자(E)_여', \
    `international_male` int(6) DEFAULT 0 COMMENT '외국인유학생(F)_남', \
    `international_female` int(6) DEFAULT 0 COMMENT '외국인유학생(F)_남', \
    `exempted_male` int(6) DEFAULT 0 COMMENT '제외인정자(G)_남', \
    `exempted_female` int(6) DEFAULT 0 COMMENT '제외인정자(G)_여', \
    `etc_male` int(6) DEFAULT 0 COMMENT '기타_남', \
    `etc_female` int(6) DEFAULT 0 COMMENT '기타_여', \
    `unknown_male` int(6) DEFAULT 0 COMMENT '미상_남', \
    `unknown_female` int(6) DEFAULT 0 COMMENT '미상_여', \
    `employment_rate` float(8, 2) DEFAULT 0.00 COMMENT '취업율(B/{A-(C+D+E+F+G)}]x100)', \
    `employed_already_male` int(6) DEFAULT 0 COMMENT '입학당시 기 취업자_남', \
    `employed_already_female` int(6) DEFAULT 0 COMMENT '입학당시 기 취업자_녀', \
    `employed_campus_male` int(6) DEFAULT 0 COMMENT '교내 취업자_남', \
    `employed_campus_female` int(6) DEFAULT 0 COMMENT '교내 취업자_여', \
    `retention_rate_1_sum` float(8, 2) DEFAULT 0.00 COMMENT '유지 취업율(수시)_1차_계', \
    `retention_rate_1_male` float(8, 2) DEFAULT 0.00 COMMENT '유지 취업율(수시)_1차_남', \
    `retention_rate_1_female` float(8, 2) DEFAULT 0.00 COMMENT '유지 취업율(수시)_1차_여', \
    `retention_rate_2_sum` float(8, 2) DEFAULT 0.00 COMMENT '유지 취업율(수시)_2차_계', \
    `retention_rate_2_male` float(8, 2) DEFAULT 0.00 COMMENT '유지 취업율(수시)_2차_남', \
    `retention_rate_2_female` float(8, 2) DEFAULT 0.00 COMMENT '유지 취업율(수시)_2차_여', \
    `retention_rate_3_sum` float(8, 2) DEFAULT 0.00 COMMENT '유지 취업율(수시)_3차_계', \
    `retention_rate_3_male` float(8, 2) DEFAULT 0.00 COMMENT '유지 취업율(수시)_3차_남', \
    `retention_rate_3_female` float(8, 2) DEFAULT 0.00 COMMENT '유지 취업율(수시)_3차_여', \
    `retention_rate_4_sum` float(8, 2) DEFAULT 0.00 COMMENT '유지 취업율(수시)_4차_계', \
    `retention_rate_4_male` float(8, 2) DEFAULT 0.00 COMMENT '유지 취업율(수시)_4차_남', \
    `retention_rate_4_female` float(8, 2) DEFAULT 0.00 COMMENT '유지 취업율(수시)_4차_여', \
    `reg_date` datetime DEFAULT CURRENT_TIMESTAMP COMMENT '생성일시',\
    `mod_date` datetime DEFAULT NULL COMMENT '수정일시',\
    PRIMARY KEY (`year`,`univ_cd`),\
    KEY `univ_cd` (`univ_cd`),\
    CONSTRAINT `graduate_employment_status_ibfk_1` FOREIGN KEY (`univ_cd`) REFERENCES `university` (`univ_cd`)\
    ) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COMMENT='졸업생의 취업 현황';"
table_dic['졸업생의 취업 현황'] = 'graduate_employment_status'





# 2023년_ [7-가. 전임교원의 연구 실적_]
#################################################
# 테이블명 : fulltime_research_achieve | 2023년_ [7-가. 전임교원의 연구 실적_]
# 전임교원_계 | 전임교원_남 | 전임교원_여 | 논문실적_총계_계 | 논문실적_총계_남 | 논문실적_총계_여 | 논문실적_국내_소계_계 | 논문실적_국내_소계_남 | 논문실적_국내_소계_여 | 논문실적_국내_연구재단 등재지(후보포함)_계 | 논문실적_국내_연구재단 등재지(후보포함)_남 | 논문실적_국내_연구재단 등재지(후보포함)_여 | 논문실적_국내_기타 일반 학술지_계 | 
#################################################
table_dic['fulltime_research_achieve'] = \
    "CREATE TABLE `fulltime_research_achieve` (\
    `year` int(4) NOT NULL COMMENT '기준연도',\
    `univ_cd` varchar(10) NOT NULL COMMENT '대학 고유코드',\
    `fulltime_tot` int(6) DEFAULT 0 COMMENT '전임교원_계', \
    `fulltime_male` int(6) DEFAULT 0 COMMENT '전임교원_남', \
    `fulltime_female` int(6) DEFAULT 0 COMMENT '전임교원_여', \
    `paper_tot_sum` float(10, 4) DEFAULT 0.00 COMMENT '논문실적_총계_계', \
    `paper_tot_male` float(10, 4) DEFAULT 0.00 COMMENT '논문실적_총계_남', \
    `paper_tot_female` float(10, 4) DEFAULT 0.00 COMMENT '논문실적_총계_여', \
    `paper_domestic_sum_tot` float(10, 4) DEFAULT 0.00 COMMENT '논문실적_국내_소계_계', \
    `paper_domestic_sum_male` float(10, 4) DEFAULT 0.00 COMMENT '논문실적_국내_소계_남', \
    `paper_domestic_sum_female` float(10, 4) DEFAULT 0.00 COMMENT '논문실적_국내_소계_여', \
    `paper_domestic_indexed_tot` float(10, 4) DEFAULT 0.00 COMMENT '논문실적_국내_연구재단 등재지(후보포함)_계', \
    `paper_domestic_indexed_male` float(10, 4) DEFAULT 0.00 COMMENT '논문실적_국내_연구재단 등재지(후보포함)_남', \
    `paper_domestic_indexed_female` float(10, 4) DEFAULT 0.00 COMMENT '논문실적_국내_연구재단 등재지(후보포함)_여', \
    `paper_domestic_academic_tot` float(10, 4) DEFAULT 0.00 COMMENT '논문실적_국내_기타 일반 학술지_계', \
    `paper_domestic_academic_male` float(10, 4) DEFAULT 0.00 COMMENT '논문실적_국내_기타 일반 학술지_남', \
    `paper_domestic_academic_female` float(10, 4) DEFAULT 0.00 COMMENT '논문실적_국내_기타 일반 학술지_여', \
    `paper_international_sum_tot` float(10, 4) DEFAULT 0.00 COMMENT '논문실적_국제_소계_계', \
    `paper_international_sum_male` float(10, 4) DEFAULT 0.00 COMMENT '논문실적_국제_소계_남', \
    `paper_international_sum_female` float(10, 4) DEFAULT 0.00 COMMENT '논문실적_국제_소계_여', \
    `paper_international_sci_tot` float(10, 4) DEFAULT 0.00 COMMENT '논문실적_국제_SCI급/SCOPUS학술지_계', \
    `paper_international_sci_male` float(10, 4) DEFAULT 0.00 COMMENT '논문실적_국제_SCI급/SCOPUS학술지_남', \
    `paper_international_sci_female` float(10, 4) DEFAULT 0.00 COMMENT '논문실적_국제_SCI급/SCOPUS학술지_여', \
    `paper_international_academic_tot` float(10, 4) DEFAULT 0.00 COMMENT '논문실적_국제_기타 일반 학술지_계', \
    `paper_international_academic_male` float(10, 4) DEFAULT 0.00 COMMENT '논문실적_국제_기타 일반 학술지_남', \
    `paper_international_academic_female` float(10, 4) DEFAULT 0.00 COMMENT '논문실적_국제_기타 일반 학술지_여', \
    `performance_tot` float(10, 4) DEFAULT 0.00 COMMENT '저역서실적_계', \
    `performance_male` float(10, 4) DEFAULT 0.00 COMMENT '저역서실적_남', \
    `performance_female` float(10, 4) DEFAULT 0.00 COMMENT '저역서실적_여', \
    `performance_book_tot` float(10, 4) DEFAULT 0.00 COMMENT '저역서실적_저서_계', \
    `performance_book_male` float(10, 4) DEFAULT 0.00 COMMENT '저역서실적_저서_남', \
    `performance_book_female` float(10, 4) DEFAULT 0.00 COMMENT '저역서실적_저서_여', \
    `performance_trans_tot` float(10, 4) DEFAULT 0.00 COMMENT '저역서실적_역서_계', \
    `performance_trans_male` float(10, 4) DEFAULT 0.00 COMMENT '저역서실적_역서_남', \
    `performance_trans_female` float(10, 4) DEFAULT 0.00 COMMENT '저역서실적_역서_여', \
    `record_domestic_tot` float(10, 4) DEFAULT 0.00 COMMENT '전임교원 1인당 논문 실적_국내_계', \
    `record_domestic_male` float(10, 4) DEFAULT 0.00 COMMENT '전임교원 1인당 논문 실적_국내_남', \
    `record_domestic_female` float(10, 4) DEFAULT 0.00 COMMENT '전임교원 1인당 논문 실적_국내_여', \
    `record_international_tot` float(10, 4) DEFAULT 0.00 COMMENT '전임교원 1인당 논문 실적_국제_계', \
    `record_international_male` float(10, 4) DEFAULT 0.00 COMMENT '전임교원 1인당 논문 실적_국제_남', \
    `record_international_female` float(10, 4) DEFAULT 0.00 COMMENT '전임교원 1인당 논문 실적_국제_여', \
    `record_indexed_tot` float(10, 4) DEFAULT 0.00 COMMENT '전임교원 1인당 논문 실적_연구재단 등재지(후보포함)_계', \
    `record_indexed_male` float(10, 4) DEFAULT 0.00 COMMENT '전임교원 1인당 논문 실적_연구재단 등재지(후보포함)_남', \
    `record_indexed_female` float(10, 4) DEFAULT 0.00 COMMENT '전임교원 1인당 논문 실적_연구재단 등재지(후보포함)_여', \
    `record_sci_tot` float(10, 4) DEFAULT 0.00 COMMENT '전임교원 1인당 논문 실적_SCI급/SCOPUS학술지_계', \
    `record_sci_male` float(10, 4) DEFAULT 0.00 COMMENT '전임교원 1인당 논문 실적_SCI급/SCOPUS학술지_남', \
    `record_sci_female` float(10, 4) DEFAULT 0.00 COMMENT '전임교원 1인당 논문 실적_SCI급/SCOPUS학술지_여', \
    `record_book_tot` float(10, 4) DEFAULT 0.00 COMMENT '전임교원 1인당 저(역)서 실적_계', \
    `record_book_male` float(10, 4) DEFAULT 0.00 COMMENT '전임교원 1인당 저(역)서 실적_남', \
    `record_book_female` float(10, 4) DEFAULT 0.00 COMMENT '전임교원 1인당 저(역)서 실적_여', \
    `reg_date` datetime DEFAULT CURRENT_TIMESTAMP COMMENT '생성일시',\
    `mod_date` datetime DEFAULT NULL COMMENT '수정일시',\
    PRIMARY KEY (`year`,`univ_cd`),\
    KEY `univ_cd` (`univ_cd`),\
    CONSTRAINT `fulltime_research_achieve_ibfk_1` FOREIGN KEY (`univ_cd`) REFERENCES `university` (`univ_cd`)\
    ) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COMMENT='전임교원의 연구 실적';"
table_dic['전임교원의 연구 실적'] = 'fulltime_research_achieve'





# 2023년_ [12-가. 연구비 수혜 실적_]
#################################################
# 테이블명 : research_fund_record | 2023년_ [12-가. 연구비 수혜 실적_]
# 전임교원_남 | 전임교원_여 | 연구비지원_계_과제_남 | 연구비지원_계_과제_여 | 연구비지원_계_연구비_남 | 연구비지원_계_연구비_여 | 연구비지원_교내_과제_남 | 연구비지원_교내_과제_여 | 연구비지원_교내_연구비_남 | 연구비지원_교내_연구비_여 | 연구비지원_교외_중앙정부_과제_남 | 연구비지원_교외_중앙정부_과제_여 | 연구비지원_교외_중앙정부_연구비_남 | 
#################################################
table_dic['research_fund_record'] = \
    "CREATE TABLE `research_fund_record` (\
    `year` int(4) NOT NULL COMMENT '기준연도',\
    `univ_cd` varchar(10) NOT NULL COMMENT '대학 고유코드',\
    `fulltime_male` int(6) DEFAULT 0 COMMENT '전임교원_남', \
    `fulltime_female` int(6) DEFAULT 0 COMMENT '전임교원_여', \
    `fund_tot_project_male` bigint(20) COMMENT '연구비지원_계_과제_남',\
    `fund_tot_project_female` bigint(20) COMMENT '연구비지원_계_과제_여',\
    `fund_tot_fund_male` bigint(20) COMMENT '연구비지원_계_연구비_남',\
    `fund_tot_fund_female` bigint(20) COMMENT '연구비지원_계_연구비_여',\
    `fund_campus_project_male` bigint(20) COMMENT '연구비지원_교내_과제_남',\
    `fund_campus_project_female` bigint(20) COMMENT '연구비지원_교내_과제_여',\
    `fund_campus_fund_male` bigint(20) COMMENT '연구비지원_교내_연구비_남',\
    `fund_campus_fund_female` bigint(20) COMMENT '연구비지원_교내_연구비_여',\
    `fund_offcampus_government_project_male` bigint(20) COMMENT '연구비지원_교외_중앙정부_과제_남',\
    `fund_offcampus_government_project_female` bigint(20) COMMENT '연구비지원_교외_중앙정부_과제_여',\
    `fund_offcampus_government_fund_male` bigint(20) COMMENT '연구비지원_교외_중앙정부_연구비_남',\
    `fund_offcampus_government_fund_female` bigint(20) COMMENT '연구비지원_교외_중앙정부_연구비_여',\
    `fund_offcampus_local_project_male` bigint(20) COMMENT '연구비지원_교외_지자체_과제_남',\
    `fund_offcampus_local_project_female` bigint(20) COMMENT '연구비지원_교외_지자체_과제_여',\
    `fund_offcampus_local_fund_male` bigint(20) COMMENT '연구비지원_교외_지자체_연구비_남',\
    `fund_offcampus_local_fund_female` bigint(20) COMMENT '연구비지원_교외_지자체_연구비_여',\
    `fund_offcampus_private_project_male` bigint(20) COMMENT '연구비지원_교외_민간_과제_남',\
    `fund_offcampus_private_project_female` bigint(20) COMMENT '연구비지원_교외_민간_과제_여',\
    `fund_offcampus_private_fund_male` bigint(20) COMMENT '연구비지원_교외_민간_연구비_남',\
    `fund_offcampus_private_fund_female` bigint(20) COMMENT '연구비지원_교외_민간_연구비_여',\
    `fund_offcampus_foreign_project_male` bigint(20) COMMENT '연구비지원_교외_외국_과제_남',\
    `fund_offcampus_foreign_project_female` bigint(20) COMMENT '연구비지원_교외_외국_과제_여',\
    `fund_offcampus_foreign_fund_male` bigint(20) COMMENT '연구비지원_교외_외국_연구비_남',\
    `fund_offcampus_foreign_fund_female` bigint(20) COMMENT '연구비지원_교외_외국_연구비_여',\
    `contingency_campus_male` bigint(20) COMMENT '대응자금_교내_남',\
    `contingency_campus_female` bigint(20) COMMENT '대응자금_교내_여',\
    `contingency_offcampus_male` bigint(20) COMMENT '대응자금_교외_남',\
    `contingency_offcampus_female` bigint(20) COMMENT '대응자금_교외_여',\
    `fund_per_1_campus_male` bigint(20) COMMENT '전임교원 1인당 연구비_교내_남',\
    `fund_per_1_campus_female` bigint(20) COMMENT '전임교원 1인당 연구비_교내_여',\
    `fund_per_1_offcampus_male` bigint(20) COMMENT '전임교원 1인당 연구비_교외_남',\
    `fund_per_1_offcampus_female` bigint(20) COMMENT '전임교원 1인당 연구비_교외_여',\
    `reg_date` datetime DEFAULT CURRENT_TIMESTAMP COMMENT '생성일시',\
    `mod_date` datetime DEFAULT NULL COMMENT '수정일시',\
    PRIMARY KEY (`year`,`univ_cd`),\
    KEY `univ_cd` (`univ_cd`),\
    CONSTRAINT `research_fund_record_ibfk_1` FOREIGN KEY (`univ_cd`) REFERENCES `university` (`univ_cd`)\
    ) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COMMENT='연구비 수혜 실적';"
table_dic['연구비 수혜 실적'] = 'research_fund_record'



# 2023년_ [12-타. 기술이전 수입료 및 계약 실적_]
#################################################
# 테이블명 : tech_transfer_income | 2023년_ [12-타. 기술이전 수입료 및 계약 실적_]
# 건수 | 수입료 (원) |  |  |  |  |  |  |  |  |  |  |  | 
#################################################
table_dic['tech_transfer_income'] = \
    "CREATE TABLE `tech_transfer_income` (\
    `year` int(4) NOT NULL COMMENT '기준연도',\
    `univ_cd` varchar(10) NOT NULL COMMENT '대학 고유코드',\
    `number_case` int(6) DEFAULT 0 COMMENT '건수', \
    `income` bigint(20) COMMENT '수입료 (원)',\
    `reg_date` datetime DEFAULT CURRENT_TIMESTAMP COMMENT '생성일시',\
    `mod_date` datetime DEFAULT NULL COMMENT '수정일시',\
    PRIMARY KEY (`year`,`univ_cd`),\
    KEY `univ_cd` (`univ_cd`),\
    CONSTRAINT `tech_transfer_income_ibfk_1` FOREIGN KEY (`univ_cd`) REFERENCES `university` (`univ_cd`)\
    ) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COMMENT='기술이전 수입료 및 계약 실적';"
table_dic['기술이전 수입료 및 계약 실적'] = 'tech_transfer_income'




# 2023년_ [12-파. 특허 출원 및 등록 실적_]
#################################################
# 테이블명 : patent_registration | 2023년_ [12-파. 특허 출원 및 등록 실적_]
# 국내특허_출원 | 국내특허_등록 | 해외특허_출원 | 해외특허_등록 |  |  |  |  |  |  |  |  |  | 
#################################################
table_dic['patent_registration'] = \
    "CREATE TABLE `patent_registration` (\
    `year` int(4) NOT NULL COMMENT '기준연도',\
    `univ_cd` varchar(10) NOT NULL COMMENT '대학 고유코드',\
    `patent_domestic_application` int(6) DEFAULT 0 COMMENT '국내특허_출원', \
    `patent_domestic_registration` int(6) DEFAULT 0 COMMENT '국내특허_등록', \
    `patent_international_application` int(6) DEFAULT 0 COMMENT '해외특허_출원', \
    `patent_international_registration` int(6) DEFAULT 0 COMMENT '해외특허_등록', \
    `reg_date` datetime DEFAULT CURRENT_TIMESTAMP COMMENT '생성일시',\
    `mod_date` datetime DEFAULT NULL COMMENT '수정일시',\
    PRIMARY KEY (`year`,`univ_cd`),\
    KEY `univ_cd` (`univ_cd`),\
    CONSTRAINT `patent_registration_ibfk_1` FOREIGN KEY (`univ_cd`) REFERENCES `university` (`univ_cd`)\
    ) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COMMENT='특허 출원 및 등록 실적';"
table_dic['특허 출원 및 등록 실적'] = 'patent_registration'




#####################################################################################################################################################################################################################################################
##################################################################################################################################################################################################################################################### 
# 4. 대학 재정, 교육
#####################################################################################################################################################################################################################################################
#####################################################################################################################################################################################################################################################

# 2023년_ [8-마-1. 자금예산서(예산)_]
#################################################
# 테이블명 : corporation_financial_budget | 2023년_ [8-마-1. 자금예산서(예산)_]
# 수입_운영수입_전입금 | 수입_운영수입_기부금 | 수입_운영수입_국고보조금 | 수입_운영수입_교육외수입 | 수입_자산및 부채수입 | 수입_미사용전기이월자금 | 수입_자금수입합계 | 지출_운영지출_보수 | 지출_운영지출_관리운영비 | 지출_운영지출_연구학생경비 | 지출_운영지출_교육외비용 | 지출_운영지출_전출금 | 지출_운영지출_예비비 | 
#################################################
table_dic['corporation_financial_budget'] = \
    "CREATE TABLE `corporation_financial_budget` (\
    `year` int(4) NOT NULL COMMENT '기준연도',\
    `univ_cd` varchar(10) NOT NULL COMMENT '대학 고유코드',\
    `income_operation_transfer` bigint(20) COMMENT '수입_운영수입_전입금',\
    `income_operation_donation` bigint(20) COMMENT '수입_운영수입_기부금',\
    `income_operation_government` bigint(20) COMMENT '수입_운영수입_국고보조금',\
    `income_operation_etc` bigint(20) COMMENT '수입_운영수입_교육외수입',\
    `income_assets_liability` bigint(20) COMMENT '수입_자산및 부채수입',\
    `income_carryover_funds` bigint(20) COMMENT '수입_미사용전기이월자금',\
    `income_fund_tot` bigint(20) COMMENT '수입_자금수입합계',\
    `expenditure_operation_compensation` bigint(20) COMMENT '지출_운영지출_보수',\
    `expenditure_operation_management` bigint(20) COMMENT '지출_운영지출_관리운영비',\
    `expenditure_operation_student` bigint(20) COMMENT '지출_운영지출_연구학생경비',\
    `expenditure_operation_etc` bigint(20) COMMENT '지출_운영지출_교육외비용',\
    `expenditure_operation_transfer` bigint(20) COMMENT '지출_운영지출_전출금',\
    `expenditure_operation_reserve` bigint(20) COMMENT '지출_운영지출_예비비',\
    `expenditure_assets_liability` bigint(20) COMMENT '지출_자산및 부채지출',\
    `expenditure_carryover_funds` bigint(20) COMMENT '지출_미사용차기이월자금',\
    `expenditure_fund_tot` bigint(20) COMMENT '지출_자금지출합계',\
    `reg_date` datetime DEFAULT CURRENT_TIMESTAMP COMMENT '생성일시',\
    `mod_date` datetime DEFAULT NULL COMMENT '수정일시',\
    PRIMARY KEY (`year`,`univ_cd`),\
    KEY `univ_cd` (`univ_cd`),\
    CONSTRAINT `corporation_financial_budget_ibfk_1` FOREIGN KEY (`univ_cd`) REFERENCES `university` (`univ_cd`)\
    ) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COMMENT='법인_자금예산서(예산)';"
table_dic['법인_자금예산서(예산)'] = 'corporation_financial_budget'



# 2023년_ [8-마-2. 자금계산서(결산)_]
#################################################
# 테이블명 : corporation_financial_settlement | 2023년_ [8-마-2. 자금계산서(결산)_]
# 수입_운영수입_전입금 | 수입_운영수입_기부금 | 수입_운영수입_국고보조금 | 수입_운영수입_교육외수입 | 수입_자산및 부채수입 | 수입_미사용전기이월자금 | 수입_자금수입합계 | 지출_운영지출_보수 | 지출_운영지출_관리운영비_업무추진비_기관장 | 지출_운영지출_관리운영비_업무추진비_상임이사 | 지출_운영지출_관리운영비_그외 운영비 | 지출_운영지출_관리운영비_운영비외 관리운영비 | 지출_운영지출_연구학생경비 | 
#################################################
table_dic['corporation_financial_settlement'] = \
    "CREATE TABLE `corporation_financial_settlement` (\
    `year` int(4) NOT NULL COMMENT '기준연도',\
    `univ_cd` varchar(10) NOT NULL COMMENT '대학 고유코드',\
    `income_operation_transfer` bigint(20) COMMENT '수입_운영수입_전입금',\
    `income_operation_donation` bigint(20) COMMENT '수입_운영수입_기부금',\
    `income_operation_government` bigint(20) COMMENT '수입_운영수입_국고보조금',\
    `income_operation_etc` bigint(20) COMMENT '수입_운영수입_교육외수입',\
    `income_assets_liability` bigint(20) COMMENT '수입_자산및 부채수입',\
    `income_carryover_funds` bigint(20) COMMENT '수입_미사용전기이월자금',\
    `income_fund_tot` bigint(20) COMMENT '수입_자금수입합계',\
    `expenditure_operation_compensation` bigint(20) COMMENT '지출_운영지출_보수',\
    `expenditure_operation_admin` bigint(20) COMMENT '지출_운영지출_관리운영비_업무추진비_기관장',\
    `expenditure_operation_director` bigint(20) COMMENT '지출_운영지출_관리운영비_업무추진비_상임이사',\
    `expenditure_operation_etc` bigint(20) COMMENT '지출_운영지출_관리운영비_그외 운영비',\
    `expenditure_operation_other_etc` bigint(20) COMMENT '지출_운영지출_관리운영비_운영비외 관리운영비',\
    `expenditure_operation_student` bigint(20) COMMENT '지출_운영지출_연구학생경비',\
    `expenditure_operation_other_education` bigint(20) COMMENT '지출_운영지출_교육외비용',\
    `expenditure_operation_transfer` bigint(20) COMMENT '지출_운영지출_전출금',\
    `expenditure_assets_liability` bigint(20) COMMENT '지출_자산및 부채지출',\
    `expenditure_carryover_funds` bigint(20) COMMENT '지출_미사용차기이월자금',\
    `expenditure_fund_tot` bigint(20) COMMENT '지출_자금지출합계',\
    `reg_date` datetime DEFAULT CURRENT_TIMESTAMP COMMENT '생성일시',\
    `mod_date` datetime DEFAULT NULL COMMENT '수정일시',\
    PRIMARY KEY (`year`,`univ_cd`),\
    KEY `univ_cd` (`univ_cd`),\
    CONSTRAINT `corporation_financial_settlement_ibfk_1` FOREIGN KEY (`univ_cd`) REFERENCES `university` (`univ_cd`)\
    ) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COMMENT='법인_자금계산서(결산)';"
table_dic['법인_자금계산서(결산)'] = 'corporation_financial_settlement'




# 2023년_ [8-마-3. 운영(손익) 계산서_]
#################################################
# 테이블명 : corporation_operating_statement | 2023년_ [8-마-3. 운영(손익) 계산서_]
# 수입_운영수입_전입금 | 수입_운영수입_기부금 | 수입_운영수입_국고보조금 | 수입_운영수입_교육외수입 | 수입_고목준비금전입액 | 수입_수익합계 | 지출_운영지출_보수 | 지출_운영지출_관리운영비 | 지출_운영지출_연구학생경비 | 지출_운영지출_교육외비용 | 지출_운영지출_전출금 | 지출_고목준비금전입액 | 지출_기본금대체액 | 
#################################################
table_dic['corporation_operating_statement'] = \
    "CREATE TABLE `corporation_operating_statement` (\
    `year` int(4) NOT NULL COMMENT '기준연도',\
    `univ_cd` varchar(10) NOT NULL COMMENT '대학 고유코드',\
    `income_operation_transfer` bigint(20) COMMENT '수입_운영수입_전입금',\
    `income_operation_donation` bigint(20) COMMENT '수입_운영수입_기부금',\
    `income_operation_government` bigint(20) COMMENT '수입_운영수입_국고보조금',\
    `income_operation_etc` bigint(20) COMMENT '수입_운영수입_교육외수입',\
    `income_specific_business` bigint(20) COMMENT '수입_고목준비금전입액',\
    `income_fund_tot` bigint(20) COMMENT '수입_수익합계',\
    `expenditure_operation_compensation` bigint(20) COMMENT '지출_운영지출_보수',\
    `expenditure_operation_management` bigint(20) COMMENT '지출_운영지출_관리운영비',\
    `expenditure_operation_student` bigint(20) COMMENT '지출_운영지출_연구학생경비',\
    `expenditure_operation_etc` bigint(20) COMMENT '지출_운영지출_교육외비용',\
    `expenditure_operation_transfer` bigint(20) COMMENT '지출_운영지출_전출금',\
    `expenditure_specific_business` bigint(20) COMMENT '지출_고목준비금전입액',\
    `expenditure_replacement` bigint(20) COMMENT '지출_기본금대체액',\
    `expenditure_replacement_variance` bigint(20) COMMENT '지출_운영차액대체액',\
    `expenditure_current_variance` bigint(20) COMMENT '지출_당기운영차액',\
    `expenditure_fund_tot` bigint(20) COMMENT '지출_지출합계',\
    `reg_date` datetime DEFAULT CURRENT_TIMESTAMP COMMENT '생성일시',\
    `mod_date` datetime DEFAULT NULL COMMENT '수정일시',\
    PRIMARY KEY (`year`,`univ_cd`),\
    KEY `univ_cd` (`univ_cd`),\
    CONSTRAINT `corporation_operating_statement_ibfk_1` FOREIGN KEY (`univ_cd`) REFERENCES `university` (`univ_cd`)\
    ) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COMMENT='법인_운영(손익) 계산서';"
table_dic['법인_운영(손익) 계산서'] = 'corporation_operating_statement'



# 2023년_ [8-마-4. 대차대조표_]
#################################################
# 테이블명 : corporation_balance_sheet | 2023년_ [8-마-4. 대차대조표_] --------------->>>>>>>>>>>>>> 2024년_ [8-마-4. 재무상태표_]
# 수입_유동자산 | 수입_투자와기타자산 | 수입_고정자산 | 수입_자산합계 | 지출_유동부채 | 지출_고정부채 | 지출_기본금 | 지출_부채와기본금 합계 |  |  |  |  |  | 
#################################################
table_dic['corporation_balance_sheet'] = \
    "CREATE TABLE `corporation_balance_sheet` (\
    `year` int(4) NOT NULL COMMENT '기준연도',\
    `univ_cd` varchar(10) NOT NULL COMMENT '대학 고유코드',\
    `income_current_assets` bigint(20) COMMENT '수입_유동자산',\
    `income_investment_assets` bigint(20) COMMENT '수입_투자와기타자산',\
    `income_fixed_assets` bigint(20) COMMENT '수입_고정자산',\
    `income_tot` bigint(20) COMMENT '수입_자산합계',\
    `expenditure_current_liabilities` bigint(20) COMMENT '지출_유동부채',\
    `expenditure_fixed_liabilities` bigint(20) COMMENT '지출_고정부채',\
    `expenditure_principal` bigint(20) COMMENT '지출_기본금',\
    `expenditure_tot` bigint(20) COMMENT '지출_부채와기본금 합계',\
    `reg_date` datetime DEFAULT CURRENT_TIMESTAMP COMMENT '생성일시',\
    `mod_date` datetime DEFAULT NULL COMMENT '수정일시',\
    PRIMARY KEY (`year`,`univ_cd`),\
    KEY `univ_cd` (`univ_cd`),\
    CONSTRAINT `corporation_balance_sheet_ibfk_1` FOREIGN KEY (`univ_cd`) REFERENCES `university` (`univ_cd`)\
    ) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COMMENT='법인_대차대조표';"
table_dic['법인_대차대조표'] = 'corporation_balance_sheet'



# 2023년_ [8-아. 기부금 현황_]
#################################################
# 테이블명 : donation_status | 2023년_ [8-아. 기부금 현황_]
# 법인회계(A) | 교비회계(B) | 산학협력단회계(C) | 당해연도 합계(D=A+B+C) | 전년도 합계(E) | 당기 증감액(F=D-E) |  |  |  |  |  |  |  | 
#################################################
table_dic['donation_status'] = \
    "CREATE TABLE `donation_status` (\
    `year` int(4) NOT NULL COMMENT '기준연도',\
    `univ_cd` varchar(10) NOT NULL COMMENT '대학 고유코드',\
    `corporate_account` bigint(20) COMMENT '법인회계(A)',\
    `school_account` bigint(20) COMMENT '교비회계(B)',\
    `cooperation_account` bigint(20) COMMENT '산학협력단회계(C)',\
    `current_year_tot` bigint(20) COMMENT '당해연도 합계(D=A+B+C)',\
    `previous_year_tot` bigint(20) COMMENT '전년도 합계(E)',\
    `current_change_amount` bigint(20) COMMENT '당기 증감액(F=D-E)',\
    `reg_date` datetime DEFAULT CURRENT_TIMESTAMP COMMENT '생성일시',\
    `mod_date` datetime DEFAULT NULL COMMENT '수정일시',\
    PRIMARY KEY (`year`,`univ_cd`),\
    KEY `univ_cd` (`univ_cd`),\
    CONSTRAINT `donation_status_ibfk_1` FOREIGN KEY (`univ_cd`) REFERENCES `university` (`univ_cd`)\
    ) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COMMENT='기부금 현황';"
table_dic['기부금 현황'] = 'donation_status'


# 2023년_ [9-나-1. 학생 1인당 교육비(국·공립대, 국립대법인, 특별법국립, 특별법법인)_]
#################################################
# 테이블명 : education_expenses_public | 2023년_ [9-나-1. 학생 1인당 교육비(국·공립대, 국립대법인, 특별법국립, 특별법법인)_]
# 대학/법인/일반회계(A) | 발전기금회계(B) | 산학협력단회계(C) | 도서구입비(D) | 기계기구매입비(E) | 총교육비(F=A+B+C+D+E) | 재학생수(G) | 학생1인당 교육비(H=F/G) |  |  |  |  |  | 
#################################################
table_dic['education_expenses_public'] = \
    "CREATE TABLE `education_expenses_public` (\
    `year` int(4) NOT NULL COMMENT '기준연도',\
    `univ_cd` varchar(10) NOT NULL COMMENT '대학 고유코드',\
    `general_account` bigint(20) COMMENT '대학/법인/일반회계(A)',\
    `development_account` bigint(20) COMMENT '발전기금회계(B)',\
    `cooperation_account` bigint(20) COMMENT '산학협력단회계(C)',\
    `book_purchase` bigint(20) COMMENT '도서구입비(D)',\
    `equipment_acquisition_cost` bigint(20) COMMENT '기계기구매입비(E)',\
    `educational_expenses_tot` bigint(20) COMMENT '총교육비(F=A+B+C+D+E)',\
    `enrolled_student` bigint(20) COMMENT '재학생수(G)',\
    `education_expenses` bigint(20) COMMENT '학생1인당 교육비(H=F/G)',\
    `reg_date` datetime DEFAULT CURRENT_TIMESTAMP COMMENT '생성일시',\
    `mod_date` datetime DEFAULT NULL COMMENT '수정일시',\
    PRIMARY KEY (`year`,`univ_cd`),\
    KEY `univ_cd` (`univ_cd`),\
    CONSTRAINT `education_expenses_public_ibfk_1` FOREIGN KEY (`univ_cd`) REFERENCES `university` (`univ_cd`)\
    ) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COMMENT='학생 1인당 교육비(국·공립대, 국립대법인, 특별법국립, 특별법법인)';"
table_dic['학생 1인당 교육비(국·공립대, 국립대법인, 특별법국립, 특별법법인)'] = 'education_expenses_public'


# 2023년_ [9-나-2. 학생 1인당 교육비(사립)_]
#################################################
# 테이블명 : education_expenses_private | 2023년_ [9-나-2. 학생 1인당 교육비(사립)_]
# 교비회계(A) | 산학협력단회계(B) | 도서구입비(C) | 기계기구매입비(D) | 총교육비(E=A+B+C+D) | 재학생수(F) | 학생1인당교육비(G=E/F) |  |  |  |  |  |  | 
#################################################
table_dic['education_expenses_private'] = \
    "CREATE TABLE `education_expenses_private` (\
    `year` int(4) NOT NULL COMMENT '기준연도',\
    `univ_cd` varchar(10) NOT NULL COMMENT '대학 고유코드',\
    `school_account` bigint(20) COMMENT '교비회계(A)',\
    `cooperation_account` bigint(20) COMMENT '산학협력단회계(B)',\
    `book_purchase` bigint(20) COMMENT '도서구입비(C)',\
    `equipment_acquisition_cost` bigint(20) COMMENT '기계기구매입비(D)',\
    `educational_expenses_tot` bigint(20) COMMENT '총교육비(E=A+B+C+D)',\
    `enrolled_student` bigint(20) COMMENT '재학생수(F)',\
    `education_expenses` bigint(20) COMMENT '학생1인당교육비(G=E/F)',\
    `reg_date` datetime DEFAULT CURRENT_TIMESTAMP COMMENT '생성일시',\
    `mod_date` datetime DEFAULT NULL COMMENT '수정일시',\
    PRIMARY KEY (`year`,`univ_cd`),\
    KEY `univ_cd` (`univ_cd`),\
    CONSTRAINT `education_expenses_private_ibfk_1` FOREIGN KEY (`univ_cd`) REFERENCES `university` (`univ_cd`)\
    ) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COMMENT='학생 1인당 교육비(사립)';"
table_dic['학생 1인당 교육비(사립)'] = 'education_expenses_private'



# 2023년_ [12-다-1. 장학금 수혜 현황_]
#################################################
# 테이블명 : scholarship_status | 2023년_ [12-다-1. 장학금 수혜 현황_]
# 재학생(A) | 장학금현황_교외_소계 | 장학금현황_교외_국가 | 장학금현황_교외_지방자치단체 | 장학금현황_교외_사설 및 기타 | 장학금현황_교내(C포함)_소계 | 장학금현황_교내(C포함)_성적우수 장학금 | 장학금현황_교내(C포함)_저소득층 장학금 | 장학금현황_교내(C포함)_근로 장학금 | 장학금현황_교내(C포함)_재난 장학금 | 장학금현황_교내(C포함)_교직원 장학금 | 장학금현황_교내(C포함)_기타 | 장학금현황_총계 | 
#################################################
table_dic['scholarship_status'] = \
    "CREATE TABLE `scholarship_status` (\
    `year` int(4) NOT NULL COMMENT '기준연도',\
    `univ_cd` varchar(10) NOT NULL COMMENT '대학 고유코드',\
    `enrolled_student` bigint(20) COMMENT '재학생(A)',\
    `scholarship_off_sum` bigint(20) COMMENT '장학금현황_교외_소계',\
    `scholarship_off_national` bigint(20) COMMENT '장학금현황_교외_국가',\
    `scholarship_off_local_government` bigint(20) COMMENT '장학금현황_교외_지방자치단체',\
    `scholarship_off_etc` bigint(20) COMMENT '장학금현황_교외_사설 및 기타',\
    `scholarship_on_sum` bigint(20) COMMENT '장학금현황_교내(C포함)_소계',\
    `scholarship_on_excellent_performance` bigint(20) COMMENT '장학금현황_교내(C포함)_성적우수 장학금',\
    `scholarship_on_low_income` bigint(20) COMMENT '장학금현황_교내(C포함)_저소득층 장학금',\
    `scholarship_on_work_study` bigint(20) COMMENT '장학금현황_교내(C포함)_근로 장학금',\
    `scholarship_on_disaster_relief` bigint(20) COMMENT '장학금현황_교내(C포함)_재난 장학금',\
    `scholarship_on_faculty` bigint(20) COMMENT '장학금현황_교내(C포함)_교직원 장학금',\
    `scholarship_on_etc` bigint(20) COMMENT '장학금현황_교내(C포함)_기타',\
    `scholarship_tot` bigint(20) COMMENT '장학금현황_총계',\
    `international_student` bigint(20) COMMENT '교내외국인유학생(외국인전형, C)',\
    `enrolled_scholarship` bigint(20) COMMENT '재학생 1인당 장학금(D=B/A)',\
    `reg_date` datetime DEFAULT CURRENT_TIMESTAMP COMMENT '생성일시',\
    `mod_date` datetime DEFAULT NULL COMMENT '수정일시',\
    PRIMARY KEY (`year`,`univ_cd`),\
    KEY `univ_cd` (`univ_cd`),\
    CONSTRAINT `scholarship_status_ibfk_1` FOREIGN KEY (`univ_cd`) REFERENCES `university` (`univ_cd`)\
    ) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COMMENT='장학금 수혜 현황';"
table_dic['장학금 수혜 현황'] = 'scholarship_status'



# 2023년_ [14-바-1. 수익용 기본재산 확보 현황_]
#################################################
# 테이블명 : revenue_assets_status | 2023년_ [14-바-1. 수익용 기본재산 확보 현황_]
# 운영수익총계(A) | 전입,기부, 원조보조수입(B) | 기준액(C) | 보유액(D) | 수익용 기본재산 확보율(D/C) x 100 | 학교운영 경비 부담 내역_수익금(E) | 학교운영 경비 부담 내역_부담액(F) | 학교운영 경비 부담 내역_부담률(%)(F/E)*100 |  |  |  |  |  | 
#################################################
table_dic['revenue_assets_status'] = \
    "CREATE TABLE `revenue_assets_status` (\
    `year` int(4) NOT NULL COMMENT '기준연도',\
    `univ_cd` varchar(10) NOT NULL COMMENT '대학 고유코드',\
    `revenue_tot` bigint(20) COMMENT '운영수익총계(A)',\
    `additional_income_sum` bigint(20) COMMENT '전입,기부, 원조보조수입(B)',\
    `standard_amount` bigint(20) COMMENT '기준액(C)',\
    `holding_amount` bigint(20) COMMENT '보유액(D)',\
    `revenue_assets_rate` float(8, 2) DEFAULT 0.00 COMMENT '수익용 기본재산 확보율(D/C) x 100', \
    `operating_revenue` bigint(20) COMMENT '학교운영 경비 부담 내역_수익금(E)',\
    `operating_burden` bigint(20) COMMENT '학교운영 경비 부담 내역_부담액(F)',\
    `operating_burden_rate` float(8, 2) DEFAULT 0.00 COMMENT '학교운영 경비 부담 내역_부담률(%)(F/E)*100', \
    `reg_date` datetime DEFAULT CURRENT_TIMESTAMP COMMENT '생성일시',\
    `mod_date` datetime DEFAULT NULL COMMENT '수정일시',\
    PRIMARY KEY (`year`,`univ_cd`),\
    KEY `univ_cd` (`univ_cd`),\
    CONSTRAINT `revenue_assets_status_ibfk_1` FOREIGN KEY (`univ_cd`) REFERENCES `university` (`univ_cd`)\
    ) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COMMENT='수익용 기본재산 확보 현황';"
table_dic['수익용 기본재산 확보 현황'] = 'revenue_assets_status'



# 2023년_ [8-바-1-(1). 교비회계(통합)_]
#################################################
# 테이블명 : school_budget_account_tot | 2023년_ [8-바-1-(1). 교비회계(통합)_]
# 수입_운영수입_등록금 및 수강료_등록금 | 수입_운영수입_등록금 및 수강료_수강료 | 수입_운영수입_전입금_법인 | 수입_운영수입_전입금_기타 | 수입_운영수입_기부금 | 수입_운영수입_국고보조금 | 수입_운영수입_산학협력단 및 학교기업전입금 | 수입_운영수입_교육부대수입 | 수입_운영수입_교육외수입 | 수입_운영수입_소계(A) | 수입_자산및부채수입(B) | 수입_미사용전기이월자금(C) | 수입_수입합계(A+B+C) | 
#################################################
table_dic['school_budget_account_tot'] = \
    "CREATE TABLE `school_budget_account_tot` (\
    `year` int(4) NOT NULL COMMENT '기준연도',\
    `univ_cd` varchar(10) NOT NULL COMMENT '대학 고유코드',\
    `income_operation_tuition_fee` bigint(20) COMMENT '수입_운영수입_등록금 및 수강료_등록금',\
    `income_operation_course_fee` bigint(20) COMMENT '수입_운영수입_등록금 및 수강료_수강료',\
    `income_operation_transfer_corporation` bigint(20) COMMENT '수입_운영수입_전입금_법인',\
    `income_operation_transfer_etc` bigint(20) COMMENT '수입_운영수입_전입금_기타',\
    `income_operation_donation` bigint(20) COMMENT '수입_운영수입_기부금',\
    `income_operation_government` bigint(20) COMMENT '수입_운영수입_국고보조금',\
    `income_operation_cooperation` bigint(20) COMMENT '수입_운영수입_산학협력단 및 학교기업전입금',\
    `income_operation_ancillary` bigint(20) COMMENT '수입_운영수입_교육부대수입',\
    `income_operation_etc` bigint(20) COMMENT '수입_운영수입_교육외수입',\
    `income_operation_sum` bigint(20) COMMENT '수입_운영수입_소계(A)',\
    `income_assets_liabilities` bigint(20) COMMENT '수입_자산및부채수입(B)',\
    `income_carryover_funds` bigint(20) COMMENT '수입_미사용전기이월자금(C)',\
    `income_tot` bigint(20) COMMENT '수입_수입합계(A+B+C)',\
    `expenditure_operation_compensation` bigint(20) COMMENT '지출_운영지출_보수',\
    `expenditure_operation_management` bigint(20) COMMENT '지출_운영지출_관리운영비',\
    `expenditure_operation_student` bigint(20) COMMENT '지출_운영지출_연구학생경비',\
    `expenditure_operation_etc` bigint(20) COMMENT '지출_운영지출_교육외비용',\
    `expenditure_operation_transfer` bigint(20) COMMENT '지출_운영지출_전출금',\
    `expenditure_operation_reserve` bigint(20) COMMENT '지출_운영지출_예비비',\
    `expenditure_operation_sum` bigint(20) COMMENT '지출_운영지출_소계(A)',\
    `expenditure_assets_liabilities` bigint(20) COMMENT '지출_자산및부채지출(B)',\
    `expenditure_carryover_funds` bigint(20) COMMENT '지출_미사용전기이월자금(C)',\
    `expenditure_tot` bigint(20) COMMENT '지출_지출합계(A+B+C)',\
    `reg_date` datetime DEFAULT CURRENT_TIMESTAMP COMMENT '생성일시',\
    `mod_date` datetime DEFAULT NULL COMMENT '수정일시',\
    PRIMARY KEY (`year`,`univ_cd`),\
    KEY `univ_cd` (`univ_cd`),\
    CONSTRAINT `school_budget_account_tot_ibfk_1` FOREIGN KEY (`univ_cd`) REFERENCES `university` (`univ_cd`)\
    ) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COMMENT='교비_예산_교비회계(통합)';"
table_dic['교비_예산_교비회계(통합)'] = 'school_budget_account_tot'




# 2023년_ [8-바-1-(2). 등록금회계_]
#################################################
# 테이블명 : school_budget_tuition_account | 2023년_ [8-바-1-(2). 등록금회계_]
# 수입_운영수입_등록금 | 수입_운영수입_전입금 | 수입_운영수입_산학협력단 및 학교기업전입금 | 수입_운영수입_교육외수입 | 수입_운영수입_소계(A) | 수입_자산및부채수입(B) | 수입_미사용전기이월자금(C) | 수입_수입합계(A+B+C) | 지출_운영지출_보수 | 지출_운영지출_관리운영비 | 지출_운영지출_연구학생경비 | 지출_운영지출_교육외비용 | 지출_운영지출_전출금 | 
#################################################
table_dic['school_budget_tuition_account'] = \
    "CREATE TABLE `school_budget_tuition_account` (\
    `year` int(4) NOT NULL COMMENT '기준연도',\
    `univ_cd` varchar(10) NOT NULL COMMENT '대학 고유코드',\
    `income_operation_tuition_fee` bigint(20) COMMENT '수입_운영수입_등록금',\
    `income_operation_transfer_fee` bigint(20) COMMENT '수입_운영수입_전입금',\
    `income_operation_cooperation` bigint(20) COMMENT '수입_운영수입_산학협력단 및 학교기업전입금',\
    `income_operation_etc` bigint(20) COMMENT '수입_운영수입_교육외수입',\
    `income_operation_sum` bigint(20) COMMENT '수입_운영수입_소계(A)',\
    `income_assets_liabilities` bigint(20) COMMENT '수입_자산및부채수입(B)',\
    `income_carryover_funds` bigint(20) COMMENT '수입_미사용전기이월자금(C)',\
    `income_tot` bigint(20) COMMENT '수입_수입합계(A+B+C)',\
    `expenditure_operation_compensation` bigint(20) COMMENT '지출_운영지출_보수',\
    `expenditure_operation_management` bigint(20) COMMENT '지출_운영지출_관리운영비',\
    `expenditure_operation_student` bigint(20) COMMENT '지출_운영지출_연구학생경비',\
    `expenditure_operation_etc` bigint(20) COMMENT '지출_운영지출_교육외비용',\
    `expenditure_operation_transfer` bigint(20) COMMENT '지출_운영지출_전출금',\
    `expenditure_operation_reserve` bigint(20) COMMENT '지출_운영지출_예비비',\
    `expenditure_operation_sum` bigint(20) COMMENT '지출_운영지출_소계(A)',\
    `expenditure_assets_liabilities` bigint(20) COMMENT '지출_자산및부채지출(B)',\
    `expenditure_carryover_funds` bigint(20) COMMENT '지출_미사용전기이월자금(C)',\
    `expenditure_tot` bigint(20) COMMENT '지출_지출합계(A+B+C)',\
    `reg_date` datetime DEFAULT CURRENT_TIMESTAMP COMMENT '생성일시',\
    `mod_date` datetime DEFAULT NULL COMMENT '수정일시',\
    PRIMARY KEY (`year`,`univ_cd`),\
    KEY `univ_cd` (`univ_cd`),\
    CONSTRAINT `school_budget_tuition_account_ibfk_1` FOREIGN KEY (`univ_cd`) REFERENCES `university` (`univ_cd`)\
    ) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COMMENT='교비_예산_등록금회계';"
table_dic['교비_예산_등록금회계'] = 'school_budget_tuition_account'


# 2023년_ [8-바-1-(3). 비등록금회계_]
#################################################
# 테이블명 : school_budget_non_tuition_account | 2023년_ [8-바-1-(3). 비등록금회계_]
# 수입_운영수입_수강료 | 수입_운영수입_전입금 | 수입_운영수입_기부금 | 수입_운영수입_국고보조금 | 수입_운영수입_교육부대수입 | 수입_운영수입_산학협력단 및 학교기업전입금 | 수입_운영수입_교육외수입 | 수입_운영수입_소계(A) | 수입_자산및부채수입(B) | 수입_미사용전기이월자금(C) | 수입_수입합계(A+B+C) | 지출_운영지출_보수 | 지출_운영지출_관리운영비 | 
#################################################
table_dic['school_budget_non_tuition_account'] = \
    "CREATE TABLE `school_budget_non_tuition_account` (\
    `year` int(4) NOT NULL COMMENT '기준연도',\
    `univ_cd` varchar(10) NOT NULL COMMENT '대학 고유코드',\
    `income_operation_tuition_fee` bigint(20) COMMENT '수입_운영수입_수강료',\
    `income_operation_transfer_fee` bigint(20) COMMENT '수입_운영수입_전입금',\
    `income_operation_donation` bigint(20) COMMENT '수입_운영수입_기부금',\
    `income_operation_government` bigint(20) COMMENT '수입_운영수입_국고보조금',\
    `income_operation_ancillary` bigint(20) COMMENT '수입_운영수입_교육부대수입',\
    `income_operation_cooperation` bigint(20) COMMENT '수입_운영수입_산학협력단 및 학교기업전입금',\
    `income_operation_etc` bigint(20) COMMENT '수입_운영수입_교육외수입',\
    `income_operation_sum` bigint(20) COMMENT '수입_운영수입_소계(A)',\
    `income_assets_liabilities` bigint(20) COMMENT '수입_자산및부채수입(B)',\
    `income_carryover_funds` bigint(20) COMMENT '수입_미사용전기이월자금(C)',\
    `income_tot` bigint(20) COMMENT '수입_수입합계(A+B+C)',\
    `expenditure_operation_compensation` bigint(20) COMMENT '지출_운영지출_보수',\
    `expenditure_operation_management` bigint(20) COMMENT '지출_운영지출_관리운영비',\
    `expenditure_operation_student` bigint(20) COMMENT '지출_운영지출_연구학생경비',\
    `expenditure_operation_etc` bigint(20) COMMENT '지출_운영지출_교육외비용',\
    `expenditure_operation_transfer` bigint(20) COMMENT '지출_운영지출_전출금',\
    `expenditure_operation_reserve` bigint(20) COMMENT '지출_운영지출_예비비',\
    `expenditure_operation_sum` bigint(20) COMMENT '지출_운영지출_소계(A)',\
    `expenditure_assets_liabilities` bigint(20) COMMENT '지출_자산및부채지출(B)',\
    `expenditure_carryover_funds` bigint(20) COMMENT '지출_미사용전기이월자금(C)',\
    `expenditure_tot` bigint(20) COMMENT '지출_지출합계(A+B+C)',\
    `reg_date` datetime DEFAULT CURRENT_TIMESTAMP COMMENT '생성일시',\
    `mod_date` datetime DEFAULT NULL COMMENT '수정일시',\
    PRIMARY KEY (`year`,`univ_cd`),\
    KEY `univ_cd` (`univ_cd`),\
    CONSTRAINT `school_budget_non_tuition_account_ibfk_1` FOREIGN KEY (`univ_cd`) REFERENCES `university` (`univ_cd`)\
    ) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COMMENT='교비_예산_비등록금회계';"
table_dic['교비_예산_비등록금회계'] = 'school_budget_non_tuition_account'




# 2023년_ [8-바-2-(1). 교비회계(통합)_]
#################################################
# 테이블명 : school_settlement_account_tot | 2023년_ [8-바-2-(1). 교비회계(통합)_]
# 수입_운영수입_등록금 및 수강료_등록금_입학금 | 수입_운영수입_등록금 및 수강료_등록금_수업료 | 수입_운영수입_등록금 및 수강료_수강료 | 수입_운영수입_전입금_법인 | 수입_운영수입_전입금_기타 | 수입_운영수입_기부금 | 수입_운영수입_국고보조금 | 수입_운영수입_산학협력단 및 학교기업전입금 | 수입_운영수입_교육부대수입 | 수입_운영수입_교육외수입 | 수입_운영수입_소계(A) | 수입_자산및부채수입(B) | 수입_미사용전기이월자금(C) | 
#################################################
table_dic['school_settlement_account_tot'] = \
    "CREATE TABLE `school_settlement_account_tot` (\
    `year` int(4) NOT NULL COMMENT '기준연도',\
    `univ_cd` varchar(10) NOT NULL COMMENT '대학 고유코드',\
    `income_operation_admission_fee` bigint(20) COMMENT '수입_운영수입_등록금 및 수강료_등록금_입학금',\
    `income_operation_tuition_fee` bigint(20) COMMENT '수입_운영수입_등록금 및 수강료_등록금_수업료',\
    `income_operation_course_fee` bigint(20) COMMENT '수입_운영수입_등록금 및 수강료_수강료',\
    `income_operation_transfer_corporation` bigint(20) COMMENT '수입_운영수입_전입금_법인',\
    `income_operation_transfer_etc` bigint(20) COMMENT '수입_운영수입_전입금_기타',\
    `income_operation_donation` bigint(20) COMMENT '수입_운영수입_기부금',\
    `income_operation_government` bigint(20) COMMENT '수입_운영수입_국고보조금',\
    `income_operation_cooperation` bigint(20) COMMENT '수입_운영수입_산학협력단 및 학교기업전입금',\
    `income_operation_ancillary` bigint(20) COMMENT '수입_운영수입_교육부대수입',\
    `income_operation_etc` bigint(20) COMMENT '수입_운영수입_교육외수입',\
    `income_operation_sum` bigint(20) COMMENT '수입_운영수입_소계(A)',\
    `income_assets_liabilities` bigint(20) COMMENT '수입_자산및부채수입(B)',\
    `income_carryover_funds` bigint(20) COMMENT '수입_미사용전기이월자금(C)',\
    `income_tot` bigint(20) COMMENT '수입_수입합계(A+B+C)',\
    `expenditure_operation_compensation` bigint(20) COMMENT '지출_운영지출_보수',\
    `expenditure_operation_management_admin` bigint(20) COMMENT '지출_운영지출_관리운영비_운영비_기관장업무추진비',\
    `expenditure_operation_management_etc` bigint(20) COMMENT '지출_운영지출_관리운영비_운영비_그 외 운영비',\
    `expenditure_operation_management_other` bigint(20) COMMENT '지출_운영지출_관리운영비_운영비 외 관리운영비',\
    `expenditure_operation_student` bigint(20) COMMENT '지출_운영지출_연구학생경비',\
    `expenditure_operation_etc` bigint(20) COMMENT '지출_운영지출_교육외비용',\
    `expenditure_operation_transfer` bigint(20) COMMENT '지출_운영지출_전출금',\
    `expenditure_operation_reserve` bigint(20) COMMENT '지출_운영지출_예비비',\
    `expenditure_operation_sum` bigint(20) COMMENT '지출_운영지출_소계(A)',\
    `expenditure_assets_liabilities` bigint(20) COMMENT '지출_자산및부채지출(B)',\
    `expenditure_carryover_funds` bigint(20) COMMENT '지출_미사용전기이월자금(C)',\
    `expenditure_tot` bigint(20) COMMENT '지출_지출합계(A+B+C)',\
    `reg_date` datetime DEFAULT CURRENT_TIMESTAMP COMMENT '생성일시',\
    `mod_date` datetime DEFAULT NULL COMMENT '수정일시',\
    PRIMARY KEY (`year`,`univ_cd`),\
    KEY `univ_cd` (`univ_cd`),\
    CONSTRAINT `school_settlement_account_tot_ibfk_1` FOREIGN KEY (`univ_cd`) REFERENCES `university` (`univ_cd`)\
    ) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COMMENT='교비_결산_교비회계(통합)';"
table_dic['교비_결산_교비회계(통합)'] = 'school_settlement_account_tot'



# 2023년_ [8-바-2-(2). 등록금회계_]
#################################################
# 테이블명 : school_settlement_tuition_account | 2023년_ [8-바-2-(2). 등록금회계_]
# 수입_운영수입_등록금_입학금 | 수입_운영수입_등록금_수업료 | 수입_운영수입_전입금_법인 | 수입_운영수입_산학협력단 및 학교기업전입금 | 수입_운영수입_교육외수입 | 수입_자산및부채수입 | 수입_미사용전기이월자금 | 수입_수입합계 | 지출_운영지출_보수 | 지출_운영지출_관리운영비_운영비_기관장업무추진비 | 지출_운영지출_관리운영비_운영비_그 외 운영비 | 지출_운영지출_관리운영비_운영비 외 관리운영비 | 지출_운영지출_연구학생경비 | 
#################################################
table_dic['school_settlement_tuition_account'] = \
    "CREATE TABLE `school_settlement_tuition_account` (\
    `year` int(4) NOT NULL COMMENT '기준연도',\
    `univ_cd` varchar(10) NOT NULL COMMENT '대학 고유코드',\
    `income_operation_admission_fee` bigint(20) COMMENT '수입_운영수입_등록금_입학금',\
    `income_operation_tuition_fee` bigint(20) COMMENT '수입_운영수입_등록금_수업료',\
    `income_operation_transfer_corporation` bigint(20) COMMENT '수입_운영수입_전입금_법인',\
    `income_operation_cooperation` bigint(20) COMMENT '수입_운영수입_산학협력단 및 학교기업전입금',\
    `income_operation_etc` bigint(20) COMMENT '수입_운영수입_교육외수입',\
    `income_assets_liabilities` bigint(20) COMMENT '수입_자산및부채수입',\
    `income_carryover_funds` bigint(20) COMMENT '수입_미사용전기이월자금',\
    `income_tot` bigint(20) COMMENT '수입_수입합계',\
    `expenditure_operation_compensation` bigint(20) COMMENT '지출_운영지출_보수',\
    `expenditure_operation_management_admin` bigint(20) COMMENT '지출_운영지출_관리운영비_운영비_기관장업무추진비',\
    `expenditure_operation_management_etc` bigint(20) COMMENT '지출_운영지출_관리운영비_운영비_그 외 운영비',\
    `expenditure_operation_management_other` bigint(20) COMMENT '지출_운영지출_관리운영비_운영비 외 관리운영비',\
    `expenditure_operation_student` bigint(20) COMMENT '지출_운영지출_연구학생경비',\
    `expenditure_operation_etc` bigint(20) COMMENT '지출_운영지출_교육외비용',\
    `expenditure_operation_transfer` bigint(20) COMMENT '지출_운영지출_전출금',\
    `expenditure_operation_reserve` bigint(20) COMMENT '지출_운영지출_예비비',\
    `expenditure_assets_liabilities` bigint(20) COMMENT '지출_자산및부채지출',\
    `expenditure_carryover_funds` bigint(20) COMMENT '지출_미사용전기이월자금',\
    `expenditure_tot` bigint(20) COMMENT '지출_지출합계',\
    `reg_date` datetime DEFAULT CURRENT_TIMESTAMP COMMENT '생성일시',\
    `mod_date` datetime DEFAULT NULL COMMENT '수정일시',\
    PRIMARY KEY (`year`,`univ_cd`),\
    KEY `univ_cd` (`univ_cd`),\
    CONSTRAINT `school_settlement_tuition_account_ibfk_1` FOREIGN KEY (`univ_cd`) REFERENCES `university` (`univ_cd`)\
    ) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COMMENT='교비_결산_등록금회계';"
table_dic['교비_결산_등록금회계'] = 'school_settlement_tuition_account'




# 2023년_ [8-바-2-(3). 비등록금회계_]
#################################################
# 테이블명 : school_settlement_non_tuition_account | 2023년_ [8-바-2-(3). 비등록금회계_]
# 수입_운영수입_수강료 | 수입_운영수입_전입금 | 수입_운영수입_기부금 | 수입_운영수입_국고보조금 | 수입_운영수입_산학협력단 및 학교기업전입금 | 수입_운영수입_교육부대수입 | 수입_운영수입_교육외수입 | 수입_자산및부채수입 | 수입_미사용전기이월자금 | 수입_수입합계 | 지출_운영지출_보수 | 지출_운영지출_관리운영비_운영비_기관장업무추진비 | 지출_운영지출_관리운영비_운영비_그 외 운영비 | 
#################################################
table_dic['school_settlement_non_tuition_account'] = \
    "CREATE TABLE `school_settlement_non_tuition_account` (\
    `year` int(4) NOT NULL COMMENT '기준연도',\
    `univ_cd` varchar(10) NOT NULL COMMENT '대학 고유코드',\
    `income_operation_tuition_fee` bigint(20) COMMENT '수입_운영수입_수강료',\
    `income_operation_transfer` bigint(20) COMMENT '수입_운영수입_전입금',\
    `income_operation_donation` bigint(20) COMMENT '수입_운영수입_기부금',\
    `income_operation_government` bigint(20) COMMENT '수입_운영수입_국고보조금',\
    `income_operation_cooperation` bigint(20) COMMENT '수입_운영수입_산학협력단 및 학교기업전입금',\
    `income_operation_ancillary` bigint(20) COMMENT '수입_운영수입_교육부대수입',\
    `income_operation_etc` bigint(20) COMMENT '수입_운영수입_교육외수입',\
    `income_assets_liabilities` bigint(20) COMMENT '수입_자산및부채수입',\
    `income_carryover_funds` bigint(20) COMMENT '수입_미사용전기이월자금',\
    `income_tot` bigint(20) COMMENT '수입_수입합계',\
    `expenditure_operation_compensation` bigint(20) COMMENT '지출_운영지출_보수',\
    `expenditure_operation_management_admin` bigint(20) COMMENT '지출_운영지출_관리운영비_운영비_기관장업무추진비',\
    `expenditure_operation_management_etc` bigint(20) COMMENT '지출_운영지출_관리운영비_운영비_그 외 운영비',\
    `expenditure_operation_management_other` bigint(20) COMMENT '지출_운영지출_관리운영비_운영비 외 관리운영비',\
    `expenditure_operation_student` bigint(20) COMMENT '지출_운영지출_연구학생경비',\
    `expenditure_operation_etc` bigint(20) COMMENT '지출_운영지출_교육외비용',\
    `expenditure_operation_transfer` bigint(20) COMMENT '지출_운영지출_전출금',\
    `expenditure_operation_reserve` bigint(20) COMMENT '지출_운영지출_예비비',\
    `expenditure_assets_liabilities` bigint(20) COMMENT '지출_자산및부채지출',\
    `expenditure_carryover_funds` bigint(20) COMMENT '지출_미사용전기이월자금',\
    `expenditure_tot` bigint(20) COMMENT '지출_지출합계',\
    `reg_date` datetime DEFAULT CURRENT_TIMESTAMP COMMENT '생성일시',\
    `mod_date` datetime DEFAULT NULL COMMENT '수정일시',\
    PRIMARY KEY (`year`,`univ_cd`),\
    KEY `univ_cd` (`univ_cd`),\
    CONSTRAINT `school_settlement_non_tuition_account_ibfk_1` FOREIGN KEY (`univ_cd`) REFERENCES `university` (`univ_cd`)\
    ) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COMMENT='교비_결산_비등록금회계';"
table_dic['교비_결산_비등록금회계'] = 'school_settlement_non_tuition_account'


# 2023년_ [8-바-3-(1). 교비회계(통합)_]
#################################################
# 테이블명 : school_operating_state_tot | 2023년_ [8-바-3-(1). 교비회계(통합)_]
# 수입_운영수입_등록금 및 수강료 | 수입_운영수입_전입금 | 수입_운영수입_기부금 | 수입_운영수입_국고보조금 | 수입_운영수입_산학협력단 및 학교기업전입금 | 수입_운영수입_교육부대수입 | 수입_운영수입_교육외수입 | 수입_고목준비금환입액 | 수입_수익합계 | 지출_운영지출_보수 | 지출_운영지출_관리운영비 | 지출_운영지출_연구학생경비 | 지출_운영지출_교육외비용 | 
#################################################
table_dic['school_operating_state_tot'] = \
    "CREATE TABLE `school_operating_state_tot` (\
    `year` int(4) NOT NULL COMMENT '기준연도',\
    `univ_cd` varchar(10) NOT NULL COMMENT '대학 고유코드',\
    `income_operation_admission_fee` bigint(20) COMMENT '수입_운영수입_등록금 및 수강료',\
    `income_operation_transfer_fee` bigint(20) COMMENT '수입_운영수입_전입금',\
    `income_operation_donation` bigint(20) COMMENT '수입_운영수입_기부금',\
    `income_operation_government` bigint(20) COMMENT '수입_운영수입_국고보조금',\
    `income_operation_cooperation` bigint(20) COMMENT '수입_운영수입_산학협력단 및 학교기업전입금',\
    `income_operation_ancillary` bigint(20) COMMENT '수입_운영수입_교육부대수입',\
    `income_operation_etc` bigint(20) COMMENT '수입_운영수입_교육외수입',\
    `income_specific_business` bigint(20) COMMENT '수입_고목준비금환입액',\
    `income_tot` bigint(20) COMMENT '수입_수익합계',\
    `expenditure_operation_compensation` bigint(20) COMMENT '지출_운영지출_보수',\
    `expenditure_operation_management` bigint(20) COMMENT '지출_운영지출_관리운영비',\
    `expenditure_operation_student` bigint(20) COMMENT '지출_운영지출_연구학생경비',\
    `expenditure_operation_etc` bigint(20) COMMENT '지출_운영지출_교육외비용',\
    `expenditure_operation_transfer` bigint(20) COMMENT '지출_운영지출_전출금',\
    `expenditure_specific_business` bigint(20) COMMENT '지출_고목준비금전입액',\
    `expenditure_replacement` bigint(20) COMMENT '지출_기본금대체액',\
    `expenditure_replacement_variance` bigint(20) COMMENT '지출_운영차액대체액',\
    `expenditure_current_variance` bigint(20) COMMENT '지출_당기운영차액',\
    `expenditure_tot` bigint(20) COMMENT '지출_지출합계',\
    `reg_date` datetime DEFAULT CURRENT_TIMESTAMP COMMENT '생성일시',\
    `mod_date` datetime DEFAULT NULL COMMENT '수정일시',\
    PRIMARY KEY (`year`,`univ_cd`),\
    KEY `univ_cd` (`univ_cd`),\
    CONSTRAINT `school_operating_state_tot_ibfk_1` FOREIGN KEY (`univ_cd`) REFERENCES `university` (`univ_cd`)\
    ) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COMMENT='교비_운영계산서_교비회계(통합)';"
table_dic['교비_운영계산서_교비회계(통합)'] = 'school_operating_state_tot'



# 2023년_ [8-바-2-(2). 등록금회계_]
#################################################
# 테이블명 : school_operating_state_tuition_account | 2023년_ [8-바-2-(2). 등록금회계_]
# 수입_운영수입_등록금 | 수입_운영수입_전입금 | 수입_운영수입_산학협력단 및 학교기업전입금 | 수입_운영수입_교육외수입 | 수입_고목준비금환입액 | 수입_수익합계 | 지출_운영지출_보수 | 지출_운영지출_관리운영비_운영비 | 지출_운영지출_연구학생경비 | 지출_운영지출_교육외비용 | 지출_운영지출_전출금 | 지출_고목준비금전입액 | 지출_기본금대체액 | 
#################################################
table_dic['school_operating_state_tuition_account'] = \
    "CREATE TABLE `school_operating_state_tuition_account` (\
    `year` int(4) NOT NULL COMMENT '기준연도',\
    `univ_cd` varchar(10) NOT NULL COMMENT '대학 고유코드',\
    `income_operation_admission_fee` bigint(20) COMMENT '수입_운영수입_등록금',\
    `income_operation_transfer_fee` bigint(20) COMMENT '수입_운영수입_전입금',\
    `income_operation_cooperation` bigint(20) COMMENT '수입_운영수입_산학협력단 및 학교기업전입금',\
    `income_operation_etc` bigint(20) COMMENT '수입_운영수입_교육외수입',\
    `income_specific_business` bigint(20) COMMENT '수입_고목준비금환입액',\
    `income_tot` bigint(20) COMMENT '수입_수익합계',\
    `expenditure_operation_compensation` bigint(20) COMMENT '지출_운영지출_보수',\
    `expenditure_operation_management` bigint(20) COMMENT '지출_운영지출_관리운영비_운영비',\
    `expenditure_operation_student` bigint(20) COMMENT '지출_운영지출_연구학생경비',\
    `expenditure_operation_etc` bigint(20) COMMENT '지출_운영지출_교육외비용',\
    `expenditure_operation_transfer` bigint(20) COMMENT '지출_운영지출_전출금',\
    `expenditure_specific_business` bigint(20) COMMENT '지출_고목준비금전입액',\
    `expenditure_replacement` bigint(20) COMMENT '지출_기본금대체액',\
    `expenditure_current_variance` bigint(20) COMMENT '지출_당기운영차액',\
    `expenditure_tot` bigint(20) COMMENT '지출_지출합계',\
    `reg_date` datetime DEFAULT CURRENT_TIMESTAMP COMMENT '생성일시',\
    `mod_date` datetime DEFAULT NULL COMMENT '수정일시',\
    PRIMARY KEY (`year`,`univ_cd`),\
    KEY `univ_cd` (`univ_cd`),\
    CONSTRAINT `school_operating_state_tuition_account_ibfk_1` FOREIGN KEY (`univ_cd`) REFERENCES `university` (`univ_cd`)\
    ) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COMMENT='교비_운영계산서_등록금회계';"
table_dic['교비_운영계산서_등록금회계'] = 'school_operating_state_tuition_account'



# 2023년_ [8-바-2-(3). 비등록금회계_]
#################################################
# 테이블명 : school_operating_state_non_tuition_account | 2023년_ [8-바-2-(3). 비등록금회계_]
# 수입_운영수입_수강료 | 수입_운영수입_전입금 | 수입_운영수입_기부금 | 수입_운영수입_국고보조금 | 수입_운영수입_산학협력단 및 학교기업전입금 | 수입_운영수입_교육부대수입 | 수입_운영수입_교육외수입 | 수입_고목준비금환입액 | 수입_수익합계 | 지출_운영지출_보수 | 지출_운영지출_관리운영비 | 지출_운영지출_연구학생경비 | 지출_운영지출_교육외비용 | 
#################################################
table_dic['school_operating_state_non_tuition_account'] = \
    "CREATE TABLE `school_operating_state_non_tuition_account` (\
    `year` int(4) NOT NULL COMMENT '기준연도',\
    `univ_cd` varchar(10) NOT NULL COMMENT '대학 고유코드',\
    `income_operation_tuition_fee` bigint(20) COMMENT '수입_운영수입_수강료',\
    `income_operation_transfer` bigint(20) COMMENT '수입_운영수입_전입금',\
    `income_operation_donation` bigint(20) COMMENT '수입_운영수입_기부금',\
    `income_operation_government` bigint(20) COMMENT '수입_운영수입_국고보조금',\
    `income_operation_cooperation` bigint(20) COMMENT '수입_운영수입_산학협력단 및 학교기업전입금',\
    `income_operation_ancillary` bigint(20) COMMENT '수입_운영수입_교육부대수입',\
    `income_operation_etc` bigint(20) COMMENT '수입_운영수입_교육외수입',\
    `income_specific_business` bigint(20) COMMENT '수입_고목준비금환입액',\
    `income_tot` bigint(20) COMMENT '수입_수익합계',\
    `expenditure_operation_compensation` bigint(20) COMMENT '지출_운영지출_보수',\
    `expenditure_operation_management` bigint(20) COMMENT '지출_운영지출_관리운영비',\
    `expenditure_operation_student` bigint(20) COMMENT '지출_운영지출_연구학생경비',\
    `expenditure_operation_etc` bigint(20) COMMENT '지출_운영지출_교육외비용',\
    `expenditure_operation_transfer` bigint(20) COMMENT '지출_운영지출_전출금',\
    `expenditure_specific_business` bigint(20) COMMENT '지출_고목준비금전입액',\
    `expenditure_replacement` bigint(20) COMMENT '지출_기본금대체액',\
    `expenditure_replacement_variance` bigint(20) COMMENT '지출_운영차액대체액',\
    `expenditure_current_variance` bigint(20) COMMENT '지출_당기운영차액',\
    `expenditure_tot` bigint(20) COMMENT '지출_지출합계',\
    `reg_date` datetime DEFAULT CURRENT_TIMESTAMP COMMENT '생성일시',\
    `mod_date` datetime DEFAULT NULL COMMENT '수정일시',\
    PRIMARY KEY (`year`,`univ_cd`),\
    KEY `univ_cd` (`univ_cd`),\
    CONSTRAINT `school_operating_state_non_tuition_account_ibfk_1` FOREIGN KEY (`univ_cd`) REFERENCES `university` (`univ_cd`)\
    ) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COMMENT='교비_운영계산서_비등록금회계';"
table_dic['교비_운영계산서_비등록금회계'] = 'school_operating_state_non_tuition_account'





# 2023년_ [8-바-4-(1). 교비회계(통합)_]
#################################################
# 테이블명 : school_balance_sheet_tot | 2023년_ [8-바-4-(1). 교비회계(통합)_]
# 수입_유동자산 | 수입_투자와기타자산 | 수입_고정자산 | 수입_자산합계 | 지출_유동부채_단기차입금 | 지출_유동부채_예수금 | 지출_유동부채_선수금 | 지출_유동부채_기타유동부채 | 지출_고정부채 | 지출_기본금 | 지출_부채와기본금 합계 |  |  | 
#################################################
table_dic['school_balance_sheet_tot'] = \
    "CREATE TABLE `school_balance_sheet_tot` (\
    `year` int(4) NOT NULL COMMENT '기준연도',\
    `univ_cd` varchar(10) NOT NULL COMMENT '대학 고유코드',\
    `income_current_assets` bigint(20) COMMENT '수입_유동자산',\
    `income_investment_assets` bigint(20) COMMENT '수입_투자와기타자산',\
    `income_fixed_assets` bigint(20) COMMENT '수입_고정자산',\
    `income_tot` bigint(20) COMMENT '수입_자산합계',\
    `expenditure_current_liabilities_short_borrow` bigint(20) COMMENT '지출_유동부채_단기차입금',\
    `expenditure_current_liabilities_deposit` bigint(20) COMMENT '지출_유동부채_예수금',\
    `expenditure_current_liabilities_advance` bigint(20) COMMENT '지출_유동부채_선수금',\
    `expenditure_current_liabilities_etc` bigint(20) COMMENT '지출_유동부채_기타유동부채',\
    `expenditure_fixed_liabilities` bigint(20) COMMENT '지출_고정부채',\
    `expenditure_principal` bigint(20) COMMENT '지출_기본금',\
    `expenditure_tot` bigint(20) COMMENT '지출_부채와기본금 합계',\
    `reg_date` datetime DEFAULT CURRENT_TIMESTAMP COMMENT '생성일시',\
    `mod_date` datetime DEFAULT NULL COMMENT '수정일시',\
    PRIMARY KEY (`year`,`univ_cd`),\
    KEY `univ_cd` (`univ_cd`),\
    CONSTRAINT `school_balance_sheet_tot_ibfk_1` FOREIGN KEY (`univ_cd`) REFERENCES `university` (`univ_cd`)\
    ) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COMMENT='교비_대차대조표_교비회계(통합)';"
table_dic['교비_대차대조표_교비회계(통합)'] = 'school_balance_sheet_tot'


# 2023년_ [8-바-4-(2). 등록금회계_]
#################################################
# 테이블명 : school_balance_sheet_tuition_account | 2023년_ [8-바-4-(2). 등록금회계_]
# 수입_유동자산 | 수입_투자와기타자산 | 수입_고정자산 | 수입_자산합계 | 지출_유동부채 | 지출_고정부채 | 지출_기본금 | 지출_부채와기본금 합계 |  |  |  |  |  | 
#################################################
table_dic['school_balance_sheet_tuition_account'] = \
    "CREATE TABLE `school_balance_sheet_tuition_account` (\
    `year` int(4) NOT NULL COMMENT '기준연도',\
    `univ_cd` varchar(10) NOT NULL COMMENT '대학 고유코드',\
    `income_current_assets` bigint(20) COMMENT '수입_유동자산',\
    `income_investment_assets` bigint(20) COMMENT '수입_투자와기타자산',\
    `income_fixed_assets` bigint(20) COMMENT '수입_고정자산',\
    `income_tot` bigint(20) COMMENT '수입_자산합계',\
    `expenditure_current_liabilities` bigint(20) COMMENT '지출_유동부채',\
    `expenditure_fixed_liabilities` bigint(20) COMMENT '지출_고정부채',\
    `expenditure_principal` bigint(20) COMMENT '지출_기본금',\
    `expenditure_tot` bigint(20) COMMENT '지출_부채와기본금 합계',\
    `reg_date` datetime DEFAULT CURRENT_TIMESTAMP COMMENT '생성일시',\
    `mod_date` datetime DEFAULT NULL COMMENT '수정일시',\
    PRIMARY KEY (`year`,`univ_cd`),\
    KEY `univ_cd` (`univ_cd`),\
    CONSTRAINT `school_balance_sheet_tuition_account_ibfk_1` FOREIGN KEY (`univ_cd`) REFERENCES `university` (`univ_cd`)\
    ) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COMMENT='교비_대차대조표_등록금회계';"
table_dic['교비_대차대조표_등록금회계'] = 'school_balance_sheet_tuition_account'



# 2023년_ [8-바-4-(3). 비등록금회계_]
#################################################
# 테이블명 : school_balance_sheet_non_tuition_account | 2023년_ [8-바-4-(3). 비등록금회계_]
# 수입_유동자산 | 수입_투자와기타자산 | 수입_고정자산 | 수입_자산합계 | 지출_유동부채 | 지출_고정부채 | 지출_기본금 | 지출_부채와기본금 합계 |  |  |  |  |  | 
#################################################
table_dic['school_balance_sheet_non_tuition_account'] = \
    "CREATE TABLE `school_balance_sheet_non_tuition_account` (\
    `year` int(4) NOT NULL COMMENT '기준연도',\
    `univ_cd` varchar(10) NOT NULL COMMENT '대학 고유코드',\
    `income_current_assets` bigint(20) COMMENT '수입_유동자산',\
    `income_investment_assets` bigint(20) COMMENT '수입_투자와기타자산',\
    `income_fixed_assets` bigint(20) COMMENT '수입_고정자산',\
    `income_tot` bigint(20) COMMENT '수입_자산합계',\
    `expenditure_current_liabilities` bigint(20) COMMENT '지출_유동부채',\
    `expenditure_fixed_liabilities` bigint(20) COMMENT '지출_고정부채',\
    `expenditure_principal` bigint(20) COMMENT '지출_기본금',\
    `expenditure_tot` bigint(20) COMMENT '지출_부채와기본금 합계',\
    `reg_date` datetime DEFAULT CURRENT_TIMESTAMP COMMENT '생성일시',\
    `mod_date` datetime DEFAULT NULL COMMENT '수정일시',\
    PRIMARY KEY (`year`,`univ_cd`),\
    KEY `univ_cd` (`univ_cd`),\
    CONSTRAINT `school_balance_sheet_non_tuition_account_ibfk_1` FOREIGN KEY (`univ_cd`) REFERENCES `university` (`univ_cd`)\
    ) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COMMENT='교비_대차대조표_비등록금회계';"
table_dic['교비_대차대조표_비등록금회계'] = 'school_balance_sheet_non_tuition_account'






#####################################################################################################################################################################################################################################################
##################################################################################################################################################################################################################################################### 
# 4. 대학 운영
#####################################################################################################################################################################################################################################################
#####################################################################################################################################################################################################################################################


# 2023년_ [14-사. 직원 현황_]
#################################################
# 테이블명 : employee_status | 2023년_ [14-사. 직원 현황_]
# 직원_특정직_남 | 직원_특정직_녀 | 직원_일반직_남 | 직원_일반직_녀 | 직원_기술직_남 | 직원_기술직_녀 | 직원_별정직_남 | 직원_별정직_녀 | 직원_기능직_남 | 직원_기능직_녀 | 직원_고용직_남 | 직원_고용직_녀 | 직원_계약직_남 | 
#################################################
table_dic['employee_status'] = \
    "CREATE TABLE `employee_status` (\
    `year` int(4) NOT NULL COMMENT '기준연도',\
    `univ_cd` varchar(10) NOT NULL COMMENT '대학 고유코드',\
    `specific_male` int(6) DEFAULT 0 COMMENT '직원_특정직_남', \
    `specific_female` int(6) DEFAULT 0 COMMENT '직원_특정직_녀', \
    `regular_male` int(6) DEFAULT 0 COMMENT '직원_일반직_남', \
    `regular_female` int(6) DEFAULT 0 COMMENT '직원_일반직_녀', \
    `technical_male` int(6) DEFAULT 0 COMMENT '직원_기술직_남', \
    `technical_female` int(6) DEFAULT 0 COMMENT '직원_기술직_녀', \
    `specialized_male` int(6) DEFAULT 0 COMMENT '직원_별정직_남', \
    `specialized_female` int(6) DEFAULT 0 COMMENT '직원_별정직_녀', \
    `functional_male` int(6) DEFAULT 0 COMMENT '직원_기능직_남', \
    `functional_female` int(6) DEFAULT 0 COMMENT '직원_기능직_녀', \
    `employment_male` int(6) DEFAULT 0 COMMENT '직원_고용직_남', \
    `employment_female` int(6) DEFAULT 0 COMMENT '직원_고용직_녀', \
    `contract_male` int(6) DEFAULT 0 COMMENT '직원_계약직_남', \
    `contract_female` int(6) DEFAULT 0 COMMENT '직원_계약직_녀', \
    `indefinite_male` int(6) DEFAULT 0 COMMENT '직원_무기계약직_남', \
    `indefinite_female` int(6) DEFAULT 0 COMMENT '직원_무기계약직_녀', \
    `etc_male` int(6) DEFAULT 0 COMMENT '직원_기타_남', \
    `etc_female` int(6) DEFAULT 0 COMMENT '직원_기타_녀', \
    `tot_male` int(6) DEFAULT 0 COMMENT '직원_총계_남', \
    `tot_female` int(6) DEFAULT 0 COMMENT '직원_총계_녀', \
    `reg_date` datetime DEFAULT CURRENT_TIMESTAMP COMMENT '생성일시',\
    `mod_date` datetime DEFAULT NULL COMMENT '수정일시',\
    PRIMARY KEY (`year`,`univ_cd`),\
    KEY `univ_cd` (`univ_cd`),\
    CONSTRAINT `employee_status_ibfk_1` FOREIGN KEY (`univ_cd`) REFERENCES `university` (`univ_cd`)\
    ) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COMMENT='직원 현황';"
table_dic['직원 현황'] = 'employee_status'



















































































###################################################################################################################################################################################
# 2. 교육 여건 - 키값이 세개 모드
###################################################################################################################################################################################




# 2023년_ [6-다-1. 국가별 외국인 전임교원 현황_]
#################################################
# 테이블명 : foreign_professor_status | 2023년_ [6-다-1. 국가별 외국인 전임교원 현황_]
# 국가별 | 전임교원_계_남 | 전임교원_계_여 | 전임교원_교수_남 | 전임교원_교수_여 | 전임교원_부교수_남 | 전임교원_부교수_여 | 전임교원_조교수_남 | 전임교원_조교수_여 |  |  |  |  | 
#################################################
table_dic['foreign_professor_status'] = \
    "CREATE TABLE `foreign_professor_status` (\
    `year` int(4) NOT NULL COMMENT '기준연도',\
    `univ_cd` varchar(10) NOT NULL COMMENT '대학 고유코드',\
    `country` varchar(200) COMMENT '국가별',\
    `fulltime_tot_male` int(6) DEFAULT 0 COMMENT '전임교원_계_남', \
    `fulltime_tot_female` int(6) DEFAULT 0 COMMENT '전임교원_계_여', \
    `fulltime_professor_male` int(6) DEFAULT 0 COMMENT '전임교원_교수_남', \
    `fulltime_professor_female` int(6) DEFAULT 0 COMMENT '전임교원_교수_여', \
    `fulltime_associate_male` int(6) DEFAULT 0 COMMENT '전임교원_부교수_남', \
    `fulltime_associate_female` int(6) DEFAULT 0 COMMENT '전임교원_부교수_여', \
    `fulltime_assistant_male` int(6) DEFAULT 0 COMMENT '전임교원_조교수_남', \
    `fulltime_assistant_female` int(6) DEFAULT 0 COMMENT '전임교원_조교수_여', \
    `reg_date` datetime DEFAULT CURRENT_TIMESTAMP COMMENT '생성일시',\
    `mod_date` datetime DEFAULT NULL COMMENT '수정일시',\
    PRIMARY KEY (`year`, `univ_cd`, `country`),\
    KEY `univ_cd` (`univ_cd`),\
    CONSTRAINT `foreign_professor_status_ibfk_1` FOREIGN KEY (`univ_cd`) REFERENCES `university` (`univ_cd`)\
    ) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COMMENT='국가별 외국인 전임교원 현황';"
table_dic['국가별 외국인 전임교원 현황'] = 'foreign_professor_status'




# 2023년_ [6-다-2. 전공계열별 외국인 전임교원 현황_]
#################################################
# 테이블명 : foreign_professor_department_status | 2023년_ [6-다-2. 전공계열별 외국인 전임교원 현황_]
# 계열 | 전임교원_계_남 | 전임교원_계_여 | 전임교원_교수_남 | 전임교원_교수_여 | 전임교원_부교수_남 | 전임교원_부교수_여 | 전임교원_조교수_남 | 전임교원_조교수_여 |  |  |  |  | 
#################################################
table_dic['foreign_professor_department_status'] = \
    "CREATE TABLE `foreign_professor_department_status` (\
    `year` int(4) NOT NULL COMMENT '기준연도',\
    `univ_cd` varchar(10) NOT NULL COMMENT '대학 고유코드',\
    `department` varchar(200) COMMENT '계열',\
    `fulltime_tot_male` int(6) DEFAULT 0 COMMENT '전임교원_계_남', \
    `fulltime_tot_female` int(6) DEFAULT 0 COMMENT '전임교원_계_여', \
    `fulltime_professor_male` int(6) DEFAULT 0 COMMENT '전임교원_교수_남', \
    `fulltime_professor_female` int(6) DEFAULT 0 COMMENT '전임교원_교수_여', \
    `fulltime_associate_male` int(6) DEFAULT 0 COMMENT '전임교원_부교수_남', \
    `fulltime_associate_female` int(6) DEFAULT 0 COMMENT '전임교원_부교수_여', \
    `fulltime_assistant_male` int(6) DEFAULT 0 COMMENT '전임교원_조교수_남', \
    `fulltime_assistant_female` int(6) DEFAULT 0 COMMENT '전임교원_조교수_여', \
    `reg_date` datetime DEFAULT CURRENT_TIMESTAMP COMMENT '생성일시',\
    `mod_date` datetime DEFAULT NULL COMMENT '수정일시',\
    PRIMARY KEY (`year`, `univ_cd`, `department`),\
    KEY `univ_cd` (`univ_cd`),\
    CONSTRAINT `foreign_professor_department_status_ibfk_1` FOREIGN KEY (`univ_cd`) REFERENCES `university` (`univ_cd`)\
    ) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COMMENT='전공계열별 외국인 전임교원 현황';"
table_dic['전공계열별 외국인 전임교원 현황'] = 'foreign_professor_department_status'



# 2023년_ [12-나-1. 학생 규모별 강좌수_]
#################################################
# 테이블명 : course_by_enrollment_size | 2023년_ [12-나-1. 학생 규모별 강좌수_]
# 학기 | 총 강좌 수 | 학생 규모별 강좌수_20명 이하 | 학생 규모별 강좌수_21~30명 | 학생 규모별 강좌수_31~40명 | 학생 규모별 강좌수_41~50명 | 학생 규모별 강좌수_51~60명 | 학생 규모별 강좌수_61~80명 | 학생 규모별 강좌수_81~100명 | 학생 규모별 강좌수_101~200명 | 학생 규모별 강좌수_201명 이상 |  |  | 
#################################################
table_dic['course_by_enrollment_size'] = \
    "CREATE TABLE `course_by_enrollment_size` (\
    `year` int(4) NOT NULL COMMENT '기준연도',\
    `univ_cd` varchar(10) NOT NULL COMMENT '대학 고유코드',\
    `semester` varchar(200) COMMENT '학기',\
    `course_tot` int(6) DEFAULT 0 COMMENT '총 강좌 수', \
    `course_per_student_size_1_20` int(6) DEFAULT 0 COMMENT '학생 규모별 강좌수_20명 이하', \
    `course_per_student_size_21_30` int(6) DEFAULT 0 COMMENT '학생 규모별 강좌수_21~30명', \
    `course_per_student_size_31_40` int(6) DEFAULT 0 COMMENT '학생 규모별 강좌수_31~40명', \
    `course_per_student_size_41_50` int(6) DEFAULT 0 COMMENT '학생 규모별 강좌수_41~50명', \
    `course_per_student_size_51_60` int(6) DEFAULT 0 COMMENT '학생 규모별 강좌수_51~60명', \
    `course_per_student_size_61_80` int(6) DEFAULT 0 COMMENT '학생 규모별 강좌수_61~80명', \
    `course_per_student_size_81_100` int(6) DEFAULT 0 COMMENT '학생 규모별 강좌수_81~100명', \
    `course_per_student_size_101_200` int(6) DEFAULT 0 COMMENT '학생 규모별 강좌수_101~200명', \
    `course_per_student_size_201_up` int(6) DEFAULT 0 COMMENT '학생 규모별 강좌수_201명 이상', \
    `reg_date` datetime DEFAULT CURRENT_TIMESTAMP COMMENT '생성일시',\
    `mod_date` datetime DEFAULT NULL COMMENT '수정일시',\
    PRIMARY KEY (`year`, `univ_cd`, `semester`),\
    KEY `univ_cd` (`univ_cd`),\
    CONSTRAINT `course_by_enrollment_size_ibfk_1` FOREIGN KEY (`univ_cd`) REFERENCES `university` (`univ_cd`)\
    ) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COMMENT='학생 규모별 강좌수';"
table_dic['학생 규모별 강좌수'] = 'course_by_enrollment_size'





# 2023년_ [12-나-2. 교원 강의 담당 비율_]
#################################################
# 테이블명 : lecture_responsibility_ratio | 2023년_ [12-나-2. 교원 강의 담당 비율_]
# 학기 | 전임교원_강의당 학점 | 전임교원_비율 | 비전임교원_겸임교원_강의당 학점 | 비전임교원_겸임교원_비율 | 비전임교원_초빙교원_강의당 학점 | 비전임교원_초빙교원_비율 | 비전임교원_강사_강의당 학점 | 비전임교원_강사_비율 | 비전임교원_시간강사_강의당 학점 | 비전임교원_시간강사_비율 | 비전임교원_기타_강의당 학점 | 비전임교원_기타_비율 | 
#################################################
table_dic['lecture_responsibility_ratio'] = \
    "CREATE TABLE `lecture_responsibility_ratio` (\
    `year` int(4) NOT NULL COMMENT '기준연도',\
    `univ_cd` varchar(10) NOT NULL COMMENT '대학 고유코드',\
    `semester` varchar(10) COMMENT '학기',\
    `fulltime_credits` int(6) DEFAULT 0 COMMENT '전임교원_강의당 학점', \
    `fulltime_rate` float(8, 2) DEFAULT 0.00 COMMENT '전임교원_비율', \
    `parttime_concurrent_credits` int(6) DEFAULT 0 COMMENT '비전임교원_겸임교원_강의당 학점', \
    `parttime_concurrent_rate` float(8, 2) DEFAULT 0.00 COMMENT '비전임교원_겸임교원_비율', \
    `parttime_invite_credits` int(6) DEFAULT 0 COMMENT '비전임교원_초빙교원_강의당 학점', \
    `parttime_invite_rate` float(8, 2) DEFAULT 0.00 COMMENT '비전임교원_초빙교원_비율', \
    `parttime_instructor_credits` int(6) DEFAULT 0 COMMENT '비전임교원_강사_강의당 학점', \
    `parttime_instructor_rate` float(8, 2) DEFAULT 0.00 COMMENT '비전임교원_강사_비율', \
    `parttime_time_credits` int(6) DEFAULT 0 COMMENT '비전임교원_시간강사_강의당 학점', \
    `parttime_time_rate` float(8, 2) DEFAULT 0.00 COMMENT '비전임교원_시간강사_비율', \
    `parttime_etc_credits` int(6) DEFAULT 0 COMMENT '비전임교원_기타_강의당 학점', \
    `parttime_etc_rate` float(8, 2) DEFAULT 0.00 COMMENT '비전임교원_기타_비율', \
    `parttime_credits_tot` int(6) DEFAULT 0 COMMENT '비전임교원_계_강의당 학점', \
    `parttime_rate_tot` float(8, 2) DEFAULT 0.00 COMMENT '비전임교원_계_비율', \
    `lecture_credits_tot` int(6) DEFAULT 0 COMMENT '강의담당 학점 총계', \
    `reg_date` datetime DEFAULT CURRENT_TIMESTAMP COMMENT '생성일시',\
    `mod_date` datetime DEFAULT NULL COMMENT '수정일시',\
    PRIMARY KEY (`year`, `univ_cd`, `semester`),\
    KEY `univ_cd` (`univ_cd`),\
    CONSTRAINT `lecture_responsibility_ratio_ibfk_1` FOREIGN KEY (`univ_cd`) REFERENCES `university` (`univ_cd`)\
    ) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COMMENT='교원 강의 담당 비율';"
table_dic['교원 강의 담당 비율'] = 'lecture_responsibility_ratio'





# 2023년_ [12-바. 대학의 원격강좌 현황_]
#################################################
# 테이블명 : remote_course_status | 2023년_ [12-바. 대학의 원격강좌 현황_]
# 학문분야 | 원격강좌(자교생 > 자교강좌 수강)_1학기_강좌수 | 원격강좌(자교생 > 자교강좌 수강)_1학기_수강자수 | 원격강좌(자교생 > 자교강좌 수강)_1학기_군복무 수강자수 | 원격강좌(자교생 > 자교강좌 수강)_2학기_강좌수 | 원격강좌(자교생 > 자교강좌 수강)_2학기_수강자수 | 원격강좌(자교생 > 자교강좌 수강)_2학기_군복무 수강자수 | 원격강좌(자교생 > 자교강좌 수강)_계절학기_강좌수 | 원격강좌(자교생 > 자교강좌 수강)_계절학기_수강자수 | 원격강좌(자교생 > 자교강좌 수강)_계절학기_군복무 수강자수 | 자교개설 학점교류 원격강좌(타교생 > 자교강좌 수강)_1학기_강좌수 | 자교개설 학점교류 원격강좌(타교생 > 자교강좌 수강)_1학기_수강자수 | 자교개설 학점교류 원격강좌(타교생 > 자교강좌 수강)_2학기_강좌수 | 
#################################################
table_dic['remote_course_status'] = \
    "CREATE TABLE `remote_course_status` (\
    `year` int(4) NOT NULL COMMENT '기준연도',\
    `univ_cd` varchar(10) NOT NULL COMMENT '대학 고유코드',\
    `academic_field` varchar(10) COMMENT '학문분야',\
    `remote_semester1_lecture_num` int(6) DEFAULT 0 COMMENT '원격강좌(자교생 > 자교강좌 수강)_1학기_강좌수', \
    `remote_semester1_participant_num` int(6) DEFAULT 0 COMMENT '원격강좌(자교생 > 자교강좌 수강)_1학기_수강자수', \
    `remote_semester1_military_num` int(6) DEFAULT 0 COMMENT '원격강좌(자교생 > 자교강좌 수강)_1학기_군복무 수강자수', \
    `remote_semester2_lecture_num` int(6) DEFAULT 0 COMMENT '원격강좌(자교생 > 자교강좌 수강)_2학기_강좌수', \
    `remote_semester2_participant_num` int(6) DEFAULT 0 COMMENT '원격강좌(자교생 > 자교강좌 수강)_2학기_수강자수', \
    `remote_semester2_military_num` int(6) DEFAULT 0 COMMENT '원격강좌(자교생 > 자교강좌 수강)_2학기_군복무 수강자수', \
    `remote_session_lecture_num` int(6) DEFAULT 0 COMMENT '원격강좌(자교생 > 자교강좌 수강)_계절학기_강좌수', \
    `remote_session_participant_num` int(6) DEFAULT 0 COMMENT '원격강좌(자교생 > 자교강좌 수강)_계절학기_수강자수', \
    `remote_session_military_num` int(6) DEFAULT 0 COMMENT '원격강좌(자교생 > 자교강좌 수강)_계절학기_군복무 수강자수', \
    `credit_exchange_semester1_lecture_num` int(6) DEFAULT 0 COMMENT '자교개설 학점교류 원격강좌(타교생 > 자교강좌 수강)_1학기_강좌수', \
    `credit_exchange_semester1_participant_num` int(6) DEFAULT 0 COMMENT '자교개설 학점교류 원격강좌(타교생 > 자교강좌 수강)_1학기_수강자수', \
    `credit_exchange_semester2_lecture_num` int(6) DEFAULT 0 COMMENT '자교개설 학점교류 원격강좌(타교생 > 자교강좌 수강)_2학기_강좌수', \
    `credit_exchange_semester2_participant_num` int(6) DEFAULT 0 COMMENT '자교개설 학점교류 원격강좌(타교생 > 자교강좌 수강)_2학기_수강자수', \
    `credit_exchange_session_lecture_num` int(6) DEFAULT 0 COMMENT '자교개설 학점교류 원격강좌(타교생 > 자교강좌 수강)_계절학기_강좌수', \
    `credit_exchange_session_participant_num` int(6) DEFAULT 0 COMMENT '자교개설 학점교류 원격강좌(타교생 > 자교강좌 수강)_계절학기_수강자수', \
    `shared_remote_lecture_num` int(6) DEFAULT 0 COMMENT '공동활용 원격강좌 수(우리 대학 학생 수강)', \
    `credit_exchange_affiliated_num` int(6) DEFAULT 0 COMMENT '학점교류 협약기관 수', \
    `reg_date` datetime DEFAULT CURRENT_TIMESTAMP COMMENT '생성일시',\
    `mod_date` datetime DEFAULT NULL COMMENT '수정일시',\
    PRIMARY KEY (`year`, `univ_cd`, `academic_field`),\
    KEY `univ_cd` (`univ_cd`),\
    CONSTRAINT `remote_course_status_ibfk_1` FOREIGN KEY (`univ_cd`) REFERENCES `university` (`univ_cd`)\
    ) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COMMENT='대학의 원격강좌 현황';"
table_dic['대학의 원격강좌 현황'] = 'remote_course_status'



# 2023년_ [12-차. 공동활용 연구장비 운영 현황_]
#################################################
# 테이블명 : shared_research_equipment | 2023년_ [12-차. 공동활용 연구장비 운영 현황_]
# 장비명 | 모델명 | 장비위치 | 제작사(공급사) | 구입년월 | 구입가격(원) | 설비자산사용료 수익_합계(원) | 설비자산사용료 수익_대학회계(원) | 설비자산사용료 수익_교비회계(원) | 설비자산사용료 수익_산단회계(원) | 설비자산사용료 수익_기타(원) |  |  | 
#################################################
table_dic['shared_research_equipment'] = \
    "CREATE TABLE `shared_research_equipment` (\
    `year` int(4) NOT NULL COMMENT '기준연도',\
    `univ_cd` varchar(10) NOT NULL COMMENT '대학 고유코드',\
    `equipment_name` varchar(200) COMMENT '장비명',\
    `model_name` varchar(200) COMMENT '모델명',\
    `location` varchar(200) COMMENT '장비위치',\
    `manufacturer` varchar(200) COMMENT '제작사(공급사)',\
    `purchase_date` varchar(200) COMMENT '구입년월',\
    `purchase_price` int(11) DEFAULT 0 COMMENT '구입가격(원)', \
    `usagefee_revenue_tot` int(11) DEFAULT 0 COMMENT '설비자산사용료 수익_합계(원)', \
    `usagefee_revenue_account_univ` int(11) DEFAULT 0 COMMENT '설비자산사용료 수익_대학회계(원)', \
    `usagefee_revenue_account_education` int(11) DEFAULT 0 COMMENT '설비자산사용료 수익_교비회계(원)', \
    `usagefee_revenue_account_industry` int(11) DEFAULT 0 COMMENT '설비자산사용료 수익_산단회계(원)', \
    `usagefee_revenue_etc` int(11) DEFAULT 0 COMMENT '설비자산사용료 수익_기타(원)', \
    `reg_date` datetime DEFAULT CURRENT_TIMESTAMP COMMENT '생성일시',\
    `mod_date` datetime DEFAULT NULL COMMENT '수정일시',\
    PRIMARY KEY (`year`, `univ_cd`, `equipment_name`),\
    KEY `univ_cd` (`univ_cd`),\
    CONSTRAINT `shared_research_equipment_ibfk_1` FOREIGN KEY (`univ_cd`) REFERENCES `university` (`univ_cd`)\
    ) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COMMENT='공동활용 연구장비 운영 현황';"
table_dic['공동활용 연구장비 운영 현황'] = 'shared_research_equipment'




# 2023년_ [13-나. 대학 부설 연구소 현황_]
#################################################
# 테이블명 : univ_research_institute | 2023년_ [13-나. 대학 부설 연구소 현황_]
# 연구소명 | 학문분야 | 전임 유급 연구원 | 학술행사 개최건수_국제학술대회 | 학술행사 개최건수_국내학술대회 | 학술행사 개최건수_기타 | 학술행사 개최건수_합계 |  |  |  |  |  |  | 
#################################################
table_dic['univ_research_institute'] = \
    "CREATE TABLE `univ_research_institute` (\
    `laboratory_name` varchar(200) COMMENT '연구소명',\
    `year` int(4) NOT NULL COMMENT '기준연도',\
    `univ_cd` varchar(10) NOT NULL COMMENT '대학 고유코드',\
    `academic_field` varchar(200) COMMENT '학문분야',\
    `researcher_fulltime` int(6) DEFAULT 0 COMMENT '전임 유급 연구원', \
    `conference_International` int(6) DEFAULT 0 COMMENT '학술행사 개최건수_국제학술대회', \
    `conference_domestic` int(6) DEFAULT 0 COMMENT '학술행사 개최건수_국내학술대회', \
    `conference_etc` int(6) DEFAULT 0 COMMENT '학술행사 개최건수_기타', \
    `conference_tot` int(6) DEFAULT 0 COMMENT '학술행사 개최건수_합계', \
    `reg_date` datetime DEFAULT CURRENT_TIMESTAMP COMMENT '생성일시',\
    `mod_date` datetime DEFAULT NULL COMMENT '수정일시',\
    PRIMARY KEY (`year`, `univ_cd`, `laboratory_name`),\
    KEY `univ_cd` (`univ_cd`),\
    CONSTRAINT `univ_research_institute_ibfk_1` FOREIGN KEY (`univ_cd`) REFERENCES `university` (`univ_cd`)\
    ) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COMMENT='대학 부설 연구소 현황';"
table_dic['대학 부설 연구소 현황'] = 'univ_research_institute'




# 2023년_ [14-라. 교사(校舍)시설 확보 현황_]
#################################################
# 테이블명 : building_acquisition_status | 2023년_ [14-라. 교사(校舍)시설 확보 현황_]
# 기준면적(m²)_입학정원 기준(A) | 기준면적(m²)_재학생 기준(B) | 건축물 전체 보유면적(㎡)_교사확보율 산정 면적_기본시설(C) | 건축물 전체 보유면적(㎡)_교사확보율 산정 면적_지원시설(D) | 건축물 전체 보유면적(㎡)_교사확보율 산정 면적_연구시설(E) | 건축물 전체 보유면적(㎡)_그외_부속시설 | 건축물 전체 보유면적(㎡)_그외_기타시설 | 교사시설확보율(%)_입학정원기준(C+D+E)/A*100 | 교사시설확보율(%)_재학생기준(C+D+E)/B*100 |  |  |  |  | 
#################################################
table_dic['building_acquisition_status'] = \
    "CREATE TABLE `building_acquisition_status` (\
    `year` int(4) NOT NULL COMMENT '기준연도',\
    `univ_cd` varchar(10) NOT NULL COMMENT '대학 고유코드',\
    `area_admission_capacity` int(8) DEFAULT 0 COMMENT '기준면적(m²)_입학정원 기준(A)', \
    `area_enrolled_student` int(8) DEFAULT 0 COMMENT '기준면적(m²)_재학생 기준(B)', \
    `building_acquisition_base` int(8) DEFAULT 0 COMMENT '건축물 전체 보유면적(㎡)_교사확보율 산정 면적_기본시설(C)', \
    `building_acquisition_support` int(8) DEFAULT 0 COMMENT '건축물 전체 보유면적(㎡)_교사확보율 산정 면적_지원시설(D)', \
    `building_acquisition_research` int(8) DEFAULT 0 COMMENT '건축물 전체 보유면적(㎡)_교사확보율 산정 면적_연구시설(E)', \
    `building_acquisition_etc_attached` int(8) DEFAULT 0 COMMENT '건축물 전체 보유면적(㎡)_그외_부속시설', \
    `building_acquisition_etc_other` int(8) DEFAULT 0 COMMENT '건축물 전체 보유면적(㎡)_그외_기타시설', \
    `acquisition_admission_rate` float(8, 2) DEFAULT 0.00 COMMENT '교사시설확보율(%)_입학정원기준(C+D+E)/A*100', \
    `acquisition_enrolled_rate` float(8, 2) DEFAULT 0.00 COMMENT '교사시설확보율(%)_재학생기준(C+D+E)/B*100', \
    `reg_date` datetime DEFAULT CURRENT_TIMESTAMP COMMENT '생성일시',\
    `mod_date` datetime DEFAULT NULL COMMENT '수정일시',\
    PRIMARY KEY (`year`,`univ_cd`),\
    KEY `univ_cd` (`univ_cd`),\
    CONSTRAINT `building_acquisition_status_ibfk_1` FOREIGN KEY (`univ_cd`) REFERENCES `university` (`univ_cd`)\
    ) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COMMENT='교사(校舍)시설 확보 현황';"
table_dic['교사(校舍)시설 확보 현황'] = 'building_acquisition_status'





# 2023년_ [14-마-1. 기숙사 수용 현황_]
#################################################
# 테이블명 : dormitory_status | 2023년_ [14-마-1. 기숙사 수용 현황_]
# 재학생수(A) | 총 실수 | 수용가능인원(B) | 실제 수용 인원_학위과정_내국인 | 실제 수용 인원_학위과정_외국인 | 실제 수용 인원_비학위과정_외국인 | 기숙사 수용률(C=B/Ax100) | 기숙사 지원자 수_동일지역 | 기숙사 지원자 수_타지역 | 기숙사 지원자 수_합계(D) | 입사 경쟁률(E=D/B) | 의무식 여부(O, X) | 운영 구분 | 
#################################################
table_dic['dormitory_status'] = \
    "CREATE TABLE `dormitory_status` (\
    `year` int(4) NOT NULL COMMENT '기준연도',\
    `univ_cd` varchar(10) NOT NULL COMMENT '대학 고유코드',\
    `enrolled_student_tot` int(6) DEFAULT 0 COMMENT '재학생수(A)', \
    `room_tot` int(6) DEFAULT 0 COMMENT '총 실수', \
    `available_personnel_tot` int(6) DEFAULT 0 COMMENT '수용가능인원(B)', \
    `real_personnel_degree_local` int(6) DEFAULT 0 COMMENT '실제 수용 인원_학위과정_내국인', \
    `real_personnel_degree_foreigner` int(6) DEFAULT 0 COMMENT '실제 수용 인원_학위과정_외국인', \
    `real_personnel_non_degree_foreigner` int(6) DEFAULT 0 COMMENT '실제 수용 인원_비학위과정_외국인', \
    `acceptance_rate` float(8, 2) DEFAULT 0.00 COMMENT '기숙사 수용률(C=B/Ax100)', \
    `applicant_same_area` int(6) DEFAULT 0 COMMENT '기숙사 지원자 수_동일지역', \
    `applicant_other_area` int(6) DEFAULT 0 COMMENT '기숙사 지원자 수_타지역', \
    `applicant_tot` int(6) DEFAULT 0 COMMENT '기숙사 지원자 수_합계(D)', \
    `competition_rate` float(8, 2) DEFAULT 0.00 COMMENT '입사 경쟁률(E=D/B)', \
    `obligation` varchar(50) COMMENT '의무식 여부(O, X)',\
    `operation_classification` varchar(50) COMMENT '운영 구분',\
    `dormitory_name` varchar(200) COMMENT '건물명',\
    `completion_year` int(6) DEFAULT 0 COMMENT '준공연도', \
    `room1_number` int(6) DEFAULT 0 COMMENT '1인실_실수', \
    `room1_food_fee` int(6) DEFAULT 0 COMMENT '1인실_식비', \
    `room1_dormitory_fee` int(6) DEFAULT 0 COMMENT '1인실_기숙사비', \
    `room2_number` int(6) DEFAULT 0 COMMENT '2인실_실수', \
    `room2_food_fee` int(6) DEFAULT 0 COMMENT '2인실_식비', \
    `room2_dormitory_fee` int(6) DEFAULT 0 COMMENT '2인실_기숙사비', \
    `room3_number` int(6) DEFAULT 0 COMMENT '3인실_실수', \
    `room3_food_fee` int(6) DEFAULT 0 COMMENT '3인실_식비', \
    `room3_dormitory_fee` int(6) DEFAULT 0 COMMENT '3인실_기숙사비', \
    `room4_number` int(6) DEFAULT 0 COMMENT '4인실이상_실수', \
    `room4_food_fee` int(6) DEFAULT 0 COMMENT '4인실이상_식비', \
    `room4_dormitory_fee` int(6) DEFAULT 0 COMMENT '4인실이상_기숙사비', \
    `reg_date` datetime DEFAULT CURRENT_TIMESTAMP COMMENT '생성일시',\
    `mod_date` datetime DEFAULT NULL COMMENT '수정일시',\
    PRIMARY KEY (`year`, `univ_cd`, `dormitory_name`, `room_tot`, `applicant_other_area`),\
    KEY `univ_cd` (`univ_cd`),\
    CONSTRAINT `dormitory_status_ibfk_1` FOREIGN KEY (`univ_cd`) REFERENCES `university` (`univ_cd`)\
    ) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COMMENT='기숙사 수용 현황';"
table_dic['기숙사 수용 현황'] = 'dormitory_status'







# 2023년_ [14-마-2-(2). 기숙사 운영 결과(사립_행복_민자)_]
#################################################
# 테이블명 : dormitory_result_private_univ_capital | 2023년_ [14-마-2-(2). 기숙사 운영 결과(사립_행복_민자)_]
# 기숙사형태 | 수익_기숙사비 수익 | 수익_임대료 수익 | 수익_기타 수익 | 수익_소계(A) | 비용_인건비 | 비용_위탁관리비 | 비용_공공요금 및 제세 | 비용_수선비 | 비용_감가상각비 | 비용_일반수용비 | 비용_학생경비 | 비용_학교회계 전출금 | 
#################################################
table_dic['dormitory_result_private_univ_capital'] = \
    "CREATE TABLE `dormitory_result_private_univ_capital` (\
    `year` int(4) NOT NULL COMMENT '기준연도',\
    `univ_cd` varchar(10) NOT NULL COMMENT '대학 고유코드',\
    `dormitory_type` varchar(200) COMMENT '기숙사형태',\
    `revenue_dormitory` bigint(20) COMMENT '수익_기숙사비 수익',\
    `revenue_rental` bigint(20) COMMENT '수익_임대료 수익',\
    `revenue_etc` bigint(20) COMMENT '수익_기타 수익',\
    `revenue_sum` bigint(20) COMMENT '수익_소계(A)',\
    `expense_personnel` bigint(20) COMMENT '비용_인건비',\
    `expense_consignment` bigint(20) COMMENT '비용_위탁관리비',\
    `expense_utility` bigint(20) COMMENT '비용_공공요금 및 제세',\
    `expense_repair` bigint(20) COMMENT '비용_수선비',\
    `expense_depreciation` bigint(20) COMMENT '비용_감가상각비',\
    `expense_accommodation` bigint(20) COMMENT '비용_일반수용비',\
    `expense_student` bigint(20) COMMENT '비용_학생경비',\
    `expense_transfer` bigint(20) COMMENT '비용_학교회계 전출금',\
    `expense_etc` bigint(20) COMMENT '비용_기타',\
    `expense_sum` bigint(20) COMMENT '비용_소계(B)',\
    `remark` varchar(500) COMMENT '비고',\
    `reg_date` datetime DEFAULT CURRENT_TIMESTAMP COMMENT '생성일시',\
    `mod_date` datetime DEFAULT NULL COMMENT '수정일시',\
    PRIMARY KEY (`year`, `univ_cd`, `dormitory_type`),\
    KEY `univ_cd` (`univ_cd`),\
    CONSTRAINT `dormitory_result_private_univ_capital_ibfk_1` FOREIGN KEY (`univ_cd`) REFERENCES `university` (`univ_cd`)\
    ) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COMMENT='기숙사 운영 결과(사립_행복_민자)';"
table_dic['기숙사 운영 결과(사립_행복_민자)'] = 'dormitory_result_private_univ_capital'



# 2023년_ [14-마-3. 기숙사비 납부제도 현황_]
#################################################
# 테이블명 : dormitory_payment_system | 2023년_ [14-마-3. 기숙사비 납부제도 현황_]
# 기숙사 형태 | 카드납부 실시 여부(O/X) | 현금분할납부_실시 여부(O/X) | 현금분할납부_분할 횟수 | 비고 |  |  |  |  |  |  |  |  | 
#################################################
table_dic['dormitory_payment_system'] = \
    "CREATE TABLE `dormitory_payment_system` (\
    `year` int(4) NOT NULL COMMENT '기준연도',\
    `univ_cd` varchar(10) NOT NULL COMMENT '대학 고유코드',\
    `dormitory_type` varchar(50) COMMENT '기숙사 형태',\
    `credit_card_implement` varchar(50) COMMENT '카드납부 실시 여부(O/X)',\
    `cash_split_implement` varchar(50) COMMENT '현금분할납부_실시 여부(O/X)',\
    `cash_split_frequency` varchar(50) COMMENT '현금분할납부_분할 횟수',\
    `remark` varchar(500) COMMENT '비고',\
    `reg_date` datetime DEFAULT CURRENT_TIMESTAMP COMMENT '생성일시',\
    `mod_date` datetime DEFAULT NULL COMMENT '수정일시',\
    PRIMARY KEY (`year`, `univ_cd`, `dormitory_type`),\
    KEY `univ_cd` (`univ_cd`),\
    CONSTRAINT `dormitory_payment_system_ibfk_1` FOREIGN KEY (`univ_cd`) REFERENCES `university` (`univ_cd`)\
    ) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COMMENT='기숙사비 납부제도 현황';"
table_dic['기숙사비 납부제도 현황'] = 'dormitory_payment_system'



# 2023년_ [14-카. 장애학생지원체제 구축 및 운영 현황_]
#################################################
# 테이블명 : disabled_student_support_status | 2023년_ [14-카. 장애학생지원체제 구축 및 운영 현황_]
# 구분(대학, 대학원) | 전체 재학생수 | 장애 재학생수_중증 장애_남 | 장애 재학생수_중증 장애_여 | 장애 재학생수_경증 장애_남 | 장애 재학생수_경증 장애_여 | 장애 재학생_계 | 장애인 특별전형 유무(O, X) | 장애인 특별전형 입학자 수(명) | 특별지원위원회 유무(O,X) | 장애학생 지원센터 유무(O,X) | 장애학생 지원센터 인력_센터장 | 장애학생 지원센터 인력_전담 | 
#################################################
table_dic['disabled_student_support_status'] = \
    "CREATE TABLE `disabled_student_support_status` (\
    `year` int(4) NOT NULL COMMENT '기준연도',\
    `univ_cd` varchar(10) NOT NULL COMMENT '대학 고유코드',\
    `classification` varchar(50) COMMENT '구분(대학, 대학원)',\
    `enrolled_student_tot` int(6) DEFAULT 0 COMMENT '전체 재학생수', \
    `disabled_serious_male` int(6) DEFAULT 0 COMMENT '장애 재학생수_중증 장애_남', \
    `disabled_serious_female` int(6) DEFAULT 0 COMMENT '장애 재학생수_중증 장애_여', \
    `disabled_mild_male` int(6) DEFAULT 0 COMMENT '장애 재학생수_경증 장애_남', \
    `disabled_mild_female` int(6) DEFAULT 0 COMMENT '장애 재학생수_경증 장애_여', \
    `disabled_student_tot` int(6) DEFAULT 0 COMMENT '장애 재학생_계', \
    `special_admission_support` varchar(50) COMMENT '장애인 특별전형 유무(O, X)',\
    `special_admission_entrant` int(6) DEFAULT 0 COMMENT '장애인 특별전형 입학자 수(명)', \
    `special_support_committee` varchar(50) COMMENT '특별지원위원회 유무(O,X)',\
    `support_center` varchar(50) COMMENT '장애학생 지원센터 유무(O,X)',\
    `support_center_chief` int(6) DEFAULT 0 COMMENT '장애학생 지원센터 인력_센터장', \
    `support_center_fulltime` int(6) DEFAULT 0 COMMENT '장애학생 지원센터 인력_전담', \
    `support_center_parttime` int(6) DEFAULT 0 COMMENT '장애학생 지원센터 인력_겸직', \
    `other_support_center_department_name` varchar(200) COMMENT '장애학생지원센터 외 지원인력_지원부서명',\
    `other_support_center_fulltime` int(6) DEFAULT 0 COMMENT '장애학생지원센터 외 지원인력_전담', \
    `other_support_center_parttime` int(6) DEFAULT 0 COMMENT '장애학생지원센터 외 지원인력_겸직', \
    `regulation` varchar(200) COMMENT '학칙 및 규정',\
    `disabled_program_minute` int(6) DEFAULT 0 COMMENT '장애이해 프로그램 운영시간(분)', \
    `educational_support_ministry_general` int(6) DEFAULT 0 COMMENT '장애학생 교육지원인력 수_교육부 사업 지원인력 (대응투자 포함)_일반 교육지원 인력', \
    `educational_support_ministry_professional` int(6) DEFAULT 0 COMMENT '장애학생 교육지원인력 수_교육부 사업 지원인력 (대응투자 포함)_전문 교육지원 인력', \
    `educational_support_none_ministry_general` int(6) DEFAULT 0 COMMENT '장애학생 교육지원인력 수_교육부 사업 외 대학자체 지원인력_일반 교육지원 인력', \
    `educational_support_none_ministry_professional` int(6) DEFAULT 0 COMMENT '장애학생 교육지원인력 수_교육부 사업 외 대학자체 지원인력_전문 교육지원 인력', \
    `beneficiary_student` int(6) DEFAULT 0 COMMENT '수혜 장애 학생 수', \
    `support plan_doc` varchar(200) COMMENT '장애 학생 지원 계획[한글(HWP(X))/워드(DOCX)]_문서',\
    `support plan_file` varchar(200) COMMENT '장애 학생 지원 계획[한글(HWP(X))/워드(DOCX)]_파일',\
    `support plan_pdf` varchar(200) COMMENT '장애 학생 지원 계획[한글(HWP(X))/워드(DOCX)]_pdf',\
    `reg_date` datetime DEFAULT CURRENT_TIMESTAMP COMMENT '생성일시',\
    `mod_date` datetime DEFAULT NULL COMMENT '수정일시',\
    PRIMARY KEY (`year`, `univ_cd`, `classification`),\
    KEY `univ_cd` (`univ_cd`),\
    CONSTRAINT `disabled_student_support_status_ibfk_1` FOREIGN KEY (`univ_cd`) REFERENCES `university` (`univ_cd`)\
    ) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COMMENT='장애학생지원체제 구축 및 운영 현황';"
table_dic['장애학생지원체제 구축 및 운영 현황'] = 'disabled_student_support_status'




#####################################################################################################################################################################################################################################################
##################################################################################################################################################################################################################################################### 
# 4. 대학 재정, 교육 - 키값이 세개 모드
#####################################################################################################################################################################################################################################################
#####################################################################################################################################################################################################################################################


# 2023년_ [8-사. 적립금 현황_]
#################################################
# 테이블명 : reserve_fund_status | 2023년_ [8-사. 적립금 현황_]
# 회계별 | 전기말 누계액(A) | 당기 인출액(B) | 당기 적립액(C) | 기타 증감(D) | 당기말 누계액(E=A-B+C+D) | 당기말 비율 |  |  |  |  |  |  | 
#################################################
table_dic['reserve_fund_status'] = \
    "CREATE TABLE `reserve_fund_status` (\
    `year` int(4) NOT NULL COMMENT '기준연도',\
    `univ_cd` varchar(10) NOT NULL COMMENT '대학 고유코드',\
    `account_type` varchar(50) COMMENT '회계별',\
    `previous_cumulative_amount` bigint(20) COMMENT '전기말 누계액(A)',\
    `current_withdrawal_amount` bigint(20) COMMENT '당기 인출액(B)',\
    `current_accrued_amount` bigint(20) COMMENT '당기 적립액(C)',\
    `other_changes` bigint(20) COMMENT '기타 증감(D)',\
    `current_cumulative_amount` bigint(20) COMMENT '당기말 누계액(E=A-B+C+D)',\
    `current_rate` int(6) DEFAULT 0 COMMENT '당기말 비율', \
    `reg_date` datetime DEFAULT CURRENT_TIMESTAMP COMMENT '생성일시',\
    `mod_date` datetime DEFAULT NULL COMMENT '수정일시',\
    PRIMARY KEY (`year`, `univ_cd`, `account_type`),\
    KEY `univ_cd` (`univ_cd`),\
    CONSTRAINT `reserve_fund_status_ibfk_1` FOREIGN KEY (`univ_cd`) REFERENCES `university` (`univ_cd`)\
    ) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COMMENT='적립금 현황';"
table_dic['적립금 현황'] = 'reserve_fund_status'



# 2023년_ [12-다-2. 학자금 대출 현황_]
#################################################
# 테이블명 : student_loan_status | 2023년_ [12-다-2. 학자금 대출 현황_]
# 구분 | 학기 | 재학생 | 일반상환 학자금 대출_전체(등록금+생활비)_인원 | 일반상환 학자금 대출_전체(등록금+생활비)_금액(원) | 일반상환 학자금 대출_등록금(학비)_인원 | 일반상환 학자금 대출_등록금(학비)_금액(원) | 취업 후 상환 학자금 대출_전체(등록금+생활비)_인원 | 취업 후 상환 학자금 대출_전체(등록금+생활비)_금액(원) | 취업 후 상환 학자금 대출_등록금(학비)_인원 | 취업 후 상환 학자금 대출_등록금(학비)_금액(원) | 학자금대출이용학생비율(%)_전체 | 학자금대출이용학생비율(%)_등록금 | 
#################################################
table_dic['student_loan_status'] = \
    "CREATE TABLE `student_loan_status` (\
    `year` int(4) NOT NULL COMMENT '기준연도',\
    `univ_cd` varchar(10) NOT NULL COMMENT '대학 고유코드',\
    `type` varchar(50) COMMENT '구분',\
    `semester` int(6) DEFAULT 0 COMMENT '학기', \
    `enrolled_student_tot` int(6) DEFAULT 0 COMMENT '재학생', \
    `regular_repayment_all_personnel` int(6) DEFAULT 0 COMMENT '일반상환 학자금 대출_전체(등록금+생활비)_인원', \
    `regular_repayment_all_amount` bigint(20) COMMENT '일반상환 학자금 대출_전체(등록금+생활비)_금액(원)',\
    `regular_repayment_tuition_personnel` int(6) DEFAULT 0 COMMENT '일반상환 학자금 대출_등록금(학비)_인원', \
    `regular_repayment_tuition_amount` bigint(20) COMMENT '일반상환 학자금 대출_등록금(학비)_금액(원)',\
    `employment_repayment_all_personnel` int(6) DEFAULT 0 COMMENT '취업 후 상환 학자금 대출_전체(등록금+생활비)_인원', \
    `employment_repayment_all_amount` bigint(20) COMMENT '취업 후 상환 학자금 대출_전체(등록금+생활비)_금액(원)',\
    `employment_repayment_tuition_personnel` int(6) DEFAULT 0 COMMENT '취업 후 상환 학자금 대출_등록금(학비)_인원', \
    `employment_repayment_tuition_amount` bigint(20) COMMENT '취업 후 상환 학자금 대출_등록금(학비)_금액(원)',\
    `student_loan_all_rate` float(8, 2) DEFAULT 0.00 COMMENT '학자금대출이용학생비율(%)_전체', \
    `student_loan_tuition_rate` float(8, 2) DEFAULT 0.00 COMMENT '학자금대출이용학생비율(%)_등록금', \
    `reg_date` datetime DEFAULT CURRENT_TIMESTAMP COMMENT '생성일시',\
    `mod_date` datetime DEFAULT NULL COMMENT '수정일시',\
    PRIMARY KEY (`year`, `univ_cd`, `type`, `semester`),\
    KEY `univ_cd` (`univ_cd`),\
    CONSTRAINT `student_loan_status_ibfk_1` FOREIGN KEY (`univ_cd`) REFERENCES `university` (`univ_cd`)\
    ) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COMMENT='학자금 대출 현황';"
table_dic['학자금 대출 현황'] = 'student_loan_status'



# 2023년_ [12-다-4. 학비감면 준수 여부_]
#################################################
# 테이블명 : tuition_reduction_status | 2023년_ [12-다-4. 학비감면 준수 여부_]
# 구분 | 학부_금액 | 학부_등록금 수입총액 | 대학원_금액 | 대학원_등록금 수입총액 | 학부+대학원_금액 | 학부+대학원_등록금 수입총액 |  |  |  |  |  |  | 
#################################################
table_dic['tuition_reduction_status'] = \
    "CREATE TABLE `tuition_reduction_status` (\
    `year` int(4) NOT NULL COMMENT '기준연도',\
    `univ_cd` varchar(10) NOT NULL COMMENT '대학 고유코드',\
    `type` varchar(50) COMMENT '구분',\
    `undergraduate_amount` bigint(20) COMMENT '학부_금액',\
    `undergraduate_tuition_tot` bigint(20) COMMENT '학부_등록금 수입총액',\
    `graduate_amount` bigint(20) COMMENT '대학원_금액',\
    `graduate_tuition_tot` bigint(20) COMMENT '대학원_등록금 수입총액',\
    `all_amount` bigint(20) COMMENT '학부+대학원_금액',\
    `all_tuition_tot` bigint(20) COMMENT '학부+대학원_등록금 수입총액',\
    `reg_date` datetime DEFAULT CURRENT_TIMESTAMP COMMENT '생성일시',\
    `mod_date` datetime DEFAULT NULL COMMENT '수정일시',\
    PRIMARY KEY (`year`, `univ_cd`, `type`),\
    KEY `univ_cd` (`univ_cd`),\
    CONSTRAINT `tuition_reduction_status_ibfk_1` FOREIGN KEY (`univ_cd`) REFERENCES `university` (`univ_cd`)\
    ) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COMMENT='학비감면 준수 여부';"
table_dic['학비감면 준수 여부'] = 'tuition_reduction_status'



# 2023년_ [14-바-2. 법정부담금 부담 현황_]
#################################################
# 테이블명 : legal_fee_status | 2023년_ [14-바-2. 법정부담금 부담 현황_]
# 법정부담금 기준액(A) | 법정부담금 부담액(B) | 부담율(B/A*100) |  |  |  |  |  |  |  |  |  |  | 
#################################################
table_dic['legal_fee_status'] = \
    "CREATE TABLE `legal_fee_status` (\
    `year` int(4) NOT NULL COMMENT '기준연도',\
    `univ_cd` varchar(10) NOT NULL COMMENT '대학 고유코드',\
    `legal_standard_amount` bigint(20) COMMENT '법정부담금 기준액(A)',\
    `legal_burden_amount` bigint(20) COMMENT '법정부담금 부담액(B)',\
    `legal_burden_rate` float(8, 2) DEFAULT 0.00 COMMENT '부담율(B/A*100)', \
    `reg_date` datetime DEFAULT CURRENT_TIMESTAMP COMMENT '생성일시',\
    `mod_date` datetime DEFAULT NULL COMMENT '수정일시',\
    PRIMARY KEY (`year`,`univ_cd`),\
    KEY `univ_cd` (`univ_cd`),\
    CONSTRAINT `legal_fee_status_ibfk_1` FOREIGN KEY (`univ_cd`) REFERENCES `university` (`univ_cd`)\
    ) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COMMENT='법정부담금 부담 현황';"
table_dic['법정부담금 부담 현황'] = 'legal_fee_status'


# 2023년_ [14-차. 강사 강의료_]
#################################################
# 테이블명 : instructor_fee | 2023년_ [14-차. 강사 강의료_]
# 강사구분 | 구분 | 시간당 지급기준 단가(원) | 지급인원수 | 총 강의시간 수 | 지급인원비율(%) |  |  |  |  |  |  |  | 
#################################################
table_dic['instructor_fee'] = \
    "CREATE TABLE `instructor_fee` (\
    `year` int(4) NOT NULL COMMENT '기준연도',\
    `univ_cd` varchar(10) NOT NULL COMMENT '대학 고유코드',\
    `instructor_classification` varchar(50) COMMENT '강사구분',\
    `classification` varchar(50) COMMENT '구분',\
    `hour_price` float(8, 2) DEFAULT 0 COMMENT '시간당 지급기준 단가(원)', \
    `recipients_tot` int(6) DEFAULT 0 COMMENT '지급인원수', \
    `lecture_hour_tot` int(6) DEFAULT 0 COMMENT '총 강의시간 수', \
    `recipients_rate` float(8, 2) DEFAULT 0.00 COMMENT '지급인원비율(%)', \
    `reg_date` datetime DEFAULT CURRENT_TIMESTAMP COMMENT '생성일시',\
    `mod_date` datetime DEFAULT NULL COMMENT '수정일시',\
    PRIMARY KEY (`year`, `univ_cd`, `instructor_classification`, `time classification`, `hour_price`),\
    KEY `univ_cd` (`univ_cd`),\
    CONSTRAINT `instructor_fee_ibfk_1` FOREIGN KEY (`univ_cd`) REFERENCES `university` (`univ_cd`)\
    ) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COMMENT='강사 강의료';"
table_dic['강사 강의료'] = 'instructor_fee'

#ALTER TABLE swu_external.instructor_fee CHANGE `time classification` classification varchar(50) CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci NOT NULL COMMENT '구분';
#ALTER TABLE swu_external.instructor_fee CHANGE `lecture hour_tot` lecture_hour_tot int(6) DEFAULT 0 NULL COMMENT '총 강의시간 수';







#####################################################################################################################################################################################################################################################
##################################################################################################################################################################################################################################################### 
# RINFO 데이터
#####################################################################################################################################################################################################################################################
#####################################################################################################################################################################################################################################################



# 2023년_ [0-0-0. 소장및구독자료_재학생1인당 소장도서수_]
#################################################
# 테이블명 : library_materials_number | 2023년_ [0-0-0. 소장및구독자료_재학생1인당 소장도서수_]
# 소장도서수 | 재학생수(전년도) | 재학생 1인당 소장도서수 |  |  |  |  |  |  |  |  |  |  | 
#################################################
table_dic['library_materials_number'] = \
    "CREATE TABLE `library_materials_number` (\
    `year` int(4) NOT NULL COMMENT '기준연도',\
    `univ_cd` varchar(10) NOT NULL COMMENT '대학 고유코드',\
    `book_number_tot` bigint(20) COMMENT '소장도서수',\
    `enrolled_prev` int(8) DEFAULT 0 COMMENT '재학생수(전년도)', \
    `book_number_per` float(8, 2) DEFAULT 0.00 COMMENT '재학생 1인당 소장도서수', \
    `reg_date` datetime DEFAULT CURRENT_TIMESTAMP COMMENT '생성일시',\
    `mod_date` datetime DEFAULT NULL COMMENT '수정일시',\
    PRIMARY KEY (`year`,`univ_cd`),\
    KEY `univ_cd` (`univ_cd`),\
    CONSTRAINT `library_materials_number_ibfk_1` FOREIGN KEY (`univ_cd`) REFERENCES `university` (`univ_cd`)\
    ) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COMMENT='소장및구독자료_재학생1인당 소장도서수';"
table_dic['소장및구독자료_재학생1인당 소장도서수'] = 'library_materials_number'




# 2023년_ [0-0-0. 예산및결산_재학생 1인당 연간 자료구입비_]
#################################################
# 테이블명 : settlement_acquisition_cost | 2023년_ [0-0-0. 예산및결산_재학생 1인당 연간 자료구입비_]
# 결산_대학총결산 | 결산_도서자료 구입비 | 결산_연속간행물 구입비 | 결산_비도서자료 구입비 | 결산_전자자료 구입비_전자저널 | 결산_전자자료 구입비_웹DB | 결산_전자자료 구입비_기타 | 결산_자료구입비 계 | 재학생1인당 자료구입비(결산)_자료구입비 | 재학생1인당 자료구입비(결산)_재학생수(전년도) | 재학생1인당 자료구입비(결산)_재학생 1인당 자료구입비 |  |  | 
#################################################
table_dic['settlement_acquisition_cost'] = \
    "CREATE TABLE `settlement_acquisition_cost` (\
    `year` int(4) NOT NULL COMMENT '기준연도',\
    `univ_cd` varchar(10) NOT NULL COMMENT '대학 고유코드',\
    `settlement_tot` bigint(20) COMMENT '결산_대학총결산',\
    `settlement_book` bigint(20) COMMENT '결산_도서자료 구입비',\
    `settlement_publication` bigint(20) COMMENT '결산_연속간행물 구입비',\
    `settlement_non_book` bigint(20) COMMENT '결산_비도서자료 구입비',\
    `settlement_elec_journal` bigint(20) COMMENT '결산_전자자료 구입비_전자저널',\
    `settlement_elec_webdb` bigint(20) COMMENT '결산_전자자료 구입비_웹DB',\
    `settlement_elec_etc` bigint(20) COMMENT '결산_전자자료 구입비_기타',\
    `settlement_acquisition_cost_tot` bigint(20) COMMENT '결산_자료구입비 계',\
    `per_acquisition_cost_sum` bigint(20) COMMENT '재학생1인당 자료구입비(결산)_자료구입비',\
    `per_enrolled_sum` int(8) DEFAULT 0 COMMENT '재학생1인당 자료구입비(결산)_재학생수(전년도)', \
    `per_acquisition_cost` float(10, 2) DEFAULT 0.00 COMMENT '재학생1인당 자료구입비(결산)_재학생 1인당 자료구입비', \
    `reg_date` datetime DEFAULT CURRENT_TIMESTAMP COMMENT '생성일시',\
    `mod_date` datetime DEFAULT NULL COMMENT '수정일시',\
    PRIMARY KEY (`year`,`univ_cd`),\
    KEY `univ_cd` (`univ_cd`),\
    CONSTRAINT `settlement_acquisition_cost_ibfk_1` FOREIGN KEY (`univ_cd`) REFERENCES `university` (`univ_cd`)\
    ) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COMMENT='예산및결산_재학생 1인당 연간 자료구입비';"
table_dic['예산및결산_재학생 1인당 연간 자료구입비'] = 'settlement_acquisition_cost'



# 2023년_ [0-0-0. 인적자원_재학생1000명당 도서관 직원수_]
#################################################
# 테이블명 : human_resource_library_staff | 2023년_ [0-0-0. 인적자원_재학생1000명당 도서관 직원수_]
# 정규직_전담_1급 정사서 | 정규직_전담_2급 정사서 | 정규직_전담_준사서 | 정규직_전담_미소지자 | 정규직_전담_계 | 정규직_겸직_1급 정사서 | 정규직_겸직_2급 정사서 | 정규직_겸직_준사서 | 정규직_겸직_미소지자 | 정규직_겸직_계 | 비정규직_전담_1급 정사서 | 비정규직_전담_2급 정사서 | 비정규직_전담_준사서 | 
#################################################
table_dic['human_resource_library_staff'] = \
    "CREATE TABLE `human_resource_library_staff` (\
    `year` int(4) NOT NULL COMMENT '기준연도',\
    `univ_cd` varchar(10) NOT NULL COMMENT '대학 고유코드',\
    `regular_full_1` int(6) DEFAULT 0 COMMENT '정규직_전담_1급 정사서', \
    `regular_full_2` int(6) DEFAULT 0 COMMENT '정규직_전담_2급 정사서', \
    `regular_full_assist` int(6) DEFAULT 0 COMMENT '정규직_전담_준사서', \
    `regular_full_none` int(6) DEFAULT 0 COMMENT '정규직_전담_미소지자', \
    `regular_full_sum` int(6) DEFAULT 0 COMMENT '정규직_전담_계', \
    `regular_part_1` int(6) DEFAULT 0 COMMENT '정규직_겸직_1급 정사서', \
    `regular_part_2` int(6) DEFAULT 0 COMMENT '정규직_겸직_2급 정사서', \
    `regular_part_assist` int(6) DEFAULT 0 COMMENT '정규직_겸직_준사서', \
    `regular_part_none` int(6) DEFAULT 0 COMMENT '정규직_겸직_미소지자', \
    `regular_part_sum` int(6) DEFAULT 0 COMMENT '정규직_겸직_계', \
    `non_regular_full_1` int(6) DEFAULT 0 COMMENT '비정규직_전담_1급 정사서', \
    `non_regular_full_2` int(6) DEFAULT 0 COMMENT '비정규직_전담_2급 정사서', \
    `non_regular_full_assist` int(6) DEFAULT 0 COMMENT '비정규직_전담_준사서', \
    `non_regular_full_none` int(6) DEFAULT 0 COMMENT '비정규직_전담_미소지자', \
    `non_regular_full_sum` int(6) DEFAULT 0 COMMENT '비정규직_전담_계', \
    `non_regular_part_1` int(6) DEFAULT 0 COMMENT '비정규직_겸직_1급 정사서', \
    `non_regular_part_2` int(6) DEFAULT 0 COMMENT '비정규직_겸직_2급 정사서', \
    `non_regular_part_assist` int(6) DEFAULT 0 COMMENT '비정규직_겸직_준사서', \
    `non_regular_part_none` int(6) DEFAULT 0 COMMENT '비정규직_겸직_미소지자', \
    `non_regular_part_sum` int(6) DEFAULT 0 COMMENT '비정규직_겸직_계', \
    `sum_regular_1` int(6) DEFAULT 0 COMMENT '합계_전담_1급 정사서', \
    `sum_regular_2` int(6) DEFAULT 0 COMMENT '합계_전담_2급 정사서', \
    `sum_regular_assist` int(6) DEFAULT 0 COMMENT '합계_전담_준사서', \
    `sum_regular_none` int(6) DEFAULT 0 COMMENT '합계_전담_미소지자', \
    `sum_regular_tot` float(8, 2) DEFAULT 0.00 COMMENT '합계_전담_계', \
    `sum_part_1` int(6) DEFAULT 0 COMMENT '합계_겸직_1급 정사서', \
    `sum_part_2` int(6) DEFAULT 0 COMMENT '합계_겸직_2급 정사서', \
    `sum_part_assist` int(6) DEFAULT 0 COMMENT '합계_겸직_준사서', \
    `sum_part_none` int(6) DEFAULT 0 COMMENT '합계_겸직_미소지자', \
    `sum_part_tot` int(6) DEFAULT 0 COMMENT '합계_겸직_계', \
    `tot_1` int(6) DEFAULT 0 COMMENT '총계_1급 정사서', \
    `tot_2` int(6) DEFAULT 0 COMMENT '총계_2급 정사서', \
    `tot_assist` int(6) DEFAULT 0 COMMENT '총계_준사서', \
    `tot_none` int(6) DEFAULT 0 COMMENT '총계_미소지자', \
    `tot_sum` float(8, 2) DEFAULT 0.00 COMMENT '총계_계', \
    `educational_offline_time` int(6) DEFAULT 0 COMMENT '직원교육현황_대면교육_참여시간', \
    `educational_offline_number` int(6) DEFAULT 0 COMMENT '직원교육현황_대면교육_참여인원', \
    `educational_remote_time` int(6) DEFAULT 0 COMMENT '직원교육현황_비대면실시간_참여시간', \
    `educational_remote_number` int(6) DEFAULT 0 COMMENT '직원교육현황_비대면실시간_참여인원', \
    `educational_online_time` float(8, 2) DEFAULT 0.00 COMMENT '직원교육현황_온라인교육_참여시간', \
    `educational_online_number` int(6) DEFAULT 0 COMMENT '직원교육현황_온라인교육_참여인원', \
    `per_1000_regular_lib_staff` int(6) DEFAULT 0 COMMENT '재학생 1000명당 도서관 직원수_정규직_사서', \
    `per_1000_regular_non_lib_staff` int(6) DEFAULT 0 COMMENT '재학생 1000명당 도서관 직원수_정규직_비사서', \
    `per_1000_part_lib_staff` int(6) DEFAULT 0 COMMENT '재학생 1000명당 도서관 직원수_비정규직_사서', \
    `per_1000_part_non_lib_staff` int(6) DEFAULT 0 COMMENT '재학생 1000명당 도서관 직원수_비정규직_비사서', \
    `per_1000_enrolled_stud1` int(6) DEFAULT 0 COMMENT '재학생 1000명당 도서관 직원수_재학생수(당해년도)', \
    `per_1000_lib_staff` float(8, 2) DEFAULT 0.00 COMMENT '재학생 1000명당 도서관 직원수_계', \
    `per_1000_regular_librarian` int(6) DEFAULT 0 COMMENT '재학생 1000명당 사서 직원수_정규직_사서', \
    `per_1000_regular_non_librarian` int(6) DEFAULT 0 COMMENT '재학생 1000명당 사서 직원수_정규직_비사서', \
    `per_1000_enrolled_stud2` int(6) DEFAULT 0 COMMENT '재학생 1000명당 사서 직원수_재학생수(당해년도)', \
    `per_1000_librarian` float(8, 2) DEFAULT 0.00 COMMENT '재학생 1000명당 사서 직원수_계', \
    `educational_participation_time` int(6) DEFAULT 0 COMMENT '직원 1인당 평균 교육 참여 시간_교육 참여시간', \
    `educational_library_staff_regular` int(6) DEFAULT 0 COMMENT '직원 1인당 평균 교육 참여 시간_도서관 직원수 정규직', \
    `educational_library_staff_non_regular` int(6) DEFAULT 0 COMMENT '직원 1인당 평균 교육 참여 시간_도서관 직원수 비정규직', \
    `educational_participation_time_avg` float(8, 2) DEFAULT 0.00 COMMENT '직원 1인당 평균 교육 참여 시간_직원 1인당 평균 교육 참여시간', \
    `reg_date` datetime DEFAULT CURRENT_TIMESTAMP COMMENT '생성일시',\
    `mod_date` datetime DEFAULT NULL COMMENT '수정일시',\
    PRIMARY KEY (`year`,`univ_cd`),\
    KEY `univ_cd` (`univ_cd`),\
    CONSTRAINT `human_resource_library_staff_ibfk_1` FOREIGN KEY (`univ_cd`) REFERENCES `university` (`univ_cd`)\
    ) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COMMENT='인적자원_재학생1000명당 도서관 직원수';"
table_dic['인적자원_재학생1000명당 도서관 직원수'] = 'human_resource_library_staff'
