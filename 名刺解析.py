# -*- coding: utf-8 -*-
"""
Business Card Similarity Calculator
This script extracts names, addresses, company details, and contact information
from business card OCR results, then calculates similarity with specified weights.
"""

import re
from difflib import SequenceMatcher

def extract_details(ocr_result):
    """
    Extract details from the given OCR result.
    Extracted fields: name, address, company, department, position, contact (phone/email)
    :param ocr_result: str - OCR result string
    :return: dict - Extracted details
    """
    # 正規表現パターン
    name_pattern = re.compile(r'([\u4E00-\u9FFF\u3040-\u30FF]+(?:\s*[\u4E00-\u9FFF\u3040-\u30FF]+)?)\s*[\(（]?.*[\)）]?')
    address_pattern = re.compile(r'(〒\d{3}-\d{4}.*)')
    company_pattern = re.compile(r'^(.*?株式会社.*?|.*?有限会社.*?)$', re.MULTILINE)
    department_pattern = re.compile(r'(営業部|マーケティング部|.*部|.*部門|.*課)')
    position_pattern = re.compile(r'(部長|課長|.*長|.*担当|.*係|.*窓口|.*補佐|.*役)')
    contact_pattern = re.compile(r'(TEL:.*?\d{2,}|Email:.*?@.*?\.\w+)')
    
    # 抽出
    name = name_pattern.search(ocr_result).group(1) if name_pattern.search(ocr_result) else "不明"
    address = address_pattern.search(ocr_result).group(1) if address_pattern.search(ocr_result) else "不明"
    company = company_pattern.search(ocr_result).group(1) if company_pattern.search(ocr_result) else "不明"
    department = department_pattern.search(ocr_result).group(1) if department_pattern.search(ocr_result) else "不明"
    position = position_pattern.search(ocr_result).group(1) if position_pattern.search(ocr_result) else "不明"
    contact = contact_pattern.search(ocr_result).group(1) if contact_pattern.search(ocr_result) else "不明"

    name = name.replace(' ', '').replace('　', '')
    address = address.replace(' ', '').replace('　', '')
    company = company.replace(' ', '').replace('　', '')
    department = department.replace(' ', '').replace('　', '')
    position = position.replace(' ', '').replace('　', '')
    contact = contact.replace(' ', '').replace('　', '')
    
    return {"name": name, "address": address, "company": company, "department": department, "position": position, "contact": contact}

def similarity_score(value1, value2):
    """
    Calculate the similarity between two string values.
    """
    return SequenceMatcher(None, value1, value2).ratio()

def name_similarity_strict(name1, name2):
    """
    Strict name similarity scoring.
    - Returns 1.0 for exact match.
    - Returns 0.0 for clear mismatch.
    - Penalizes partial matches significantly.
    """
    if name1 == name2:
        return 1.0  # 完全一致
    else:
        # 部分一致を許容しつつ、文字列の長さ差をペナルティに追加
        similarity = SequenceMatcher(None, name1, name2).ratio()
        length_penalty = min(len(name1), len(name2)) / max(len(name1), len(name2))
        return similarity * length_penalty 

def business_card_similarity(ocr1, ocr2):
    """
    Calculate the similarity between two business cards.
    Emphasizes name similarity with lower weights for other fields.
    """
    # 重み設定
    weights = {
        "name": 10,
        "company": 3,
        "department": 3,
        "position": 3,
        "contact": 2,
        "address": 3
    }
    
    # 抽出
    details1 = extract_details(ocr1)
    details2 = extract_details(ocr2)
    
    # 各フィールドのスコア計算
    scores = {key:name_similarity_strict(details1[key], details2[key]) if key == 'name' else similarity_score(details1[key], details2[key]) for key in details1.keys()}
    
    # 重み付け計算
    total_weight = sum(weights.values())
    weighted_similarity = sum(scores[key] * weights[key] for key in scores.keys()) / total_weight
    
    return round(weighted_similarity, 4), scores  # 全体スコアと各フィールドのスコアを返す

if __name__ == "__main__":
    # 名刺のOCR結果（名刺1）
    ocr_result1 = '''
    株式会社XYZ
    営業部 部長
    斧 太郎（おの たろう）
    〒123-4567 東京都新宿区西新宿1-1-1
    TEL: 03-1234-5678
    Email: taro.ono@xyz.co.jp
    '''
    
    # 名刺のOCR結果（名刺2）
    ocr_result2 = '''
    ABC株式会社
    マーケティング部 部長
    斧太郎
    〒987-6543 東京都港区南青山2-2-2
    TEL: 03-8765-4321
    Email: ono.taro@abc.co.jp
    '''
    
    # 名刺の類似度計算
    similarity, field_scores = business_card_similarity(ocr_result1, ocr_result2)
    
    print("Similarity Score:", similarity)
    print("Field-wise Scores:", field_scores)
