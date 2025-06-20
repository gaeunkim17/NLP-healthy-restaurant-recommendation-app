#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd
import numpy as np
import streamlit as st


# In[2]:


df = pd.read_csv('total_df.csv')


# cd C:\Users\82105\anaconda3
# streamlit run healthy_restaurant_recommendation_test.py
# healthy_restaurant_recommendation_test
# #스트림릿 실행

# 
# 
# # import streamlit as st
# import pandas as pd
# 
# # CSV 파일 불러오기
# df = pd.read_csv("total_df.csv")
# df.fillna('', inplace=True)
# 
# st.title("🍱 서울시 맞춤 건강 식당 추천")
# 
# # 전체 카테고리 목록 추출
# category_options = sorted(set(df["카테고리1"]).union(df["카테고리2"]).union(df["카테고리3"]))
# selected_categories = st.multiselect('카테고리 선택', category_options, label_visibility="collapsed")
# 
# if st.button("🔍 추천 받기", key="recommend_button"):
#     if not selected_categories:
#         st.warning("최소 하나의 카테고리를 선택하세요.")
#     else:
#         def contains_all_categories(row):
#             categories = {row["카테고리1"], row["카테고리2"], row["카테고리3"]}
#             return all(cat in categories for cat in selected_categories)
# 
#         filtered_df = df[df.apply(contains_all_categories, axis=1)].copy()
#         filtered_df = filtered_df.sort_values(by="rank")
# 
#         if filtered_df.empty:
#             st.info("선택한 모든 카테고리를 만족하는 식당이 없습니다.")
#         else:
#             st.success(f"총 {len(filtered_df)}개 식당이 추천되었습니다.")
# 
#             for idx, row in filtered_df.iterrows():
#                 box_start = """
#                 <div style='background-color: #B7E5C9;
#                             padding: 20px;
#                             border-radius: 12px;
#                             margin-bottom: 20px;
#                             width: 20px;
#                             height: 3px;'>
#                 """
#                 box_end = "</div>"
# 
#                 st.markdown(box_start, unsafe_allow_html=True)
# 
#                 # 식당명 (제목보다 작음, h2)
#                 st.markdown(f"<h2 style='margin-bottom: 10px;'>{row['식당명']}</h2>", unsafe_allow_html=True)
# 
#                 # 각 항목 제목 (h4, 약간 굵게, 약간 더 큰 글씨)
#                 st.markdown("<h4 style='font-weight:300; margin-bottom:4px;'>📌 카테고리</h4>", unsafe_allow_html=True)
#                 st.markdown(f"<div style='margin-left:20px; font-size: 16px;'>{', '.join(filter(None, [row['카테고리1'], row['카테고리2'], row['카테고리3']]))}</div>", unsafe_allow_html=True)
# 
#                 st.markdown("<h4 style='font-weight:300; margin-bottom:4px;'>📝 키워드</h4>", unsafe_allow_html=True)
#                 if row['카테고리1 키워드']:
#                     st.markdown(f"<div style='margin-left:20px; font-size: 16px;'>{row['카테고리1 키워드']}</div>", unsafe_allow_html=True)
#                 if row['카테고리2 키워드']:
#                     st.markdown(f"<div style='margin-left:20px; font-size: 16px;'>{row['카테고리2 키워드']}</div>", unsafe_allow_html=True)
#                 if row['카테고리3 키워드']:
#                     st.markdown(f"<div style='margin-left:20px; font-size: 16px;'>{row['카테고리3 키워드']}</div>", unsafe_allow_html=True)
# 
#                 st.markdown("<h4 style='font-weight:300; margin-bottom:4px;'>🍽️ 혼밥 점수</h4>", unsafe_allow_html=True)
#                 st.markdown(f"<div style='margin-left:20px; font-size: 16px;'>{row['혼밥']}</div>", unsafe_allow_html=True)
# 
#                 st.markdown("<h4 style='font-weight:300; margin-bottom:4px;'>🥡 포장 점수</h4>", unsafe_allow_html=True)
#                 st.markdown(f"<div style='margin-left:20px; font-size: 16px;'>{row['포장']}</div>", unsafe_allow_html=True)
# 
#                 st.markdown(box_end, unsafe_allow_html=True)

# In[8]:


import streamlit as st
import pandas as pd

# CSV 파일 불러오기
df = pd.read_csv("total_df.csv")
df.fillna('', inplace=True)

st.title("🍱 서울시 맞춤 건강 식당 추천")

# 전체 카테고리 목록 추출
category_options = sorted(set(df["카테고리1"]).union(df["카테고리2"]).union(df["카테고리3"]))
selected_categories = st.multiselect('카테고리 선택', category_options, label_visibility="collapsed")

if st.button("🔍 추천 받기", key="recommend_button"):
    if not selected_categories:
        st.warning("최소 하나의 카테고리를 선택하세요.")
    else:
        def contains_all_categories(row):
            categories = {row["카테고리1"], row["카테고리2"], row["카테고리3"]}
            return all(cat in categories for cat in selected_categories)

        filtered_df = df[df.apply(contains_all_categories, axis=1)].copy()
        filtered_df = filtered_df.sort_values(by="rank")

        if filtered_df.empty:
            st.info("선택한 모든 카테고리를 만족하는 식당이 없습니다.")
        else:
            st.success(f"총 {len(filtered_df)}개 식당이 추천되었습니다.")

            for idx, row in filtered_df.iterrows():
                # 식당명 (제목보다 작음, h2)
                st.markdown(f"<h2 style='margin-bottom: 10px; font-size: 20px;'>{row['식당명']}</h2>", unsafe_allow_html=True)

                # 각 항목 제목 (h4, 약간 굵게, 약간 더 큰 글씨)
                st.markdown("<h4 style='font-weight:400; margin-bottom:4px; font-size: 18px;'>📌 카테고리</h4>", unsafe_allow_html=True)
                st.markdown(f"<div style='margin-left:20px; font-size: 16px;'>{', '.join(filter(None, [row['카테고리1'], row['카테고리2'], row['카테고리3']]))}</div>", unsafe_allow_html=True)

                st.markdown("<h4 style='font-weight:400; margin-bottom:4px; font-size: 18px;'>📝 키워드</h4>", unsafe_allow_html=True)
                for kw in [row['카테고리1 키워드'], row['카테고리2 키워드'], row['카테고리3 키워드']]:
                    if kw:
                        st.markdown(f"<div style='margin-left:20px; font-size: 16px;'>{kw}</div>", unsafe_allow_html=True)

                st.markdown("<h4 style='font-weight:400; margin-bottom:4px; font-size: 18px;'>🍽️ 혼밥 점수</h4>", unsafe_allow_html=True)
                st.markdown(f"<div style='margin-left:20px; font-size: 16px;'>{row['혼밥']}</div>", unsafe_allow_html=True)

                st.markdown("<h4 style='font-weight:400; margin-bottom:4px; font-size: 18px;'>🥡 포장 점수</h4>", unsafe_allow_html=True)
                st.markdown(f"<div style='margin-left:20px; font-size: 16px;'>{row['포장']}</div>", unsafe_allow_html=True)

                # ✅ 가로선 추가
                st.markdown("<hr style='border: 1.5px solid #B7E5C9; margin: 30px 0;'>", unsafe_allow_html=True)

