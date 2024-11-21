# ライブラリのインストール
# !pip install scikit-image mahotas opencv-python opencv-contrib-python PyWavelets

import numpy as np
from PIL import Image
from scipy import ndimage
from scipy.signal import correlate2d
from skimage import feature, filters, metrics, transform
from sklearn.decomposition import PCA
from sklearn.metrics.pairwise import cosine_similarity
import pywt
import mahotas
import cv2
# from tensorflow.keras.applications.vgg16 import VGG16, preprocess_input
# from tensorflow.keras.models import Model
import time

def cosine_similarity_func(vec1, vec2):
    from numpy.linalg import norm
    return np.dot(vec1, vec2) / (norm(vec1) * norm(vec2))

def extract_contours_similarity(img1, img2):
    # エッジ検出（Canny法）
    edges1 = feature.canny(img1)
    edges2 = feature.canny(img2)
    # 類似度計算
    intersection = np.logical_and(edges1, edges2).sum()
    union = np.logical_or(edges1, edges2).sum()
    similarity = intersection / union
    return similarity

def deep_learning_similarity(img1, img2):
    # 事前学習済みモデルのロード
    base_model = VGG16(weights='imagenet')
    model = Model(inputs=base_model.input, outputs=base_model.get_layer('fc2').output)
    
    # 画像の前処理
    def preprocess(img):
        img = Image.fromarray(img).convert('RGB').resize((224, 224))
        x = np.array(img)
        x = np.expand_dims(x, axis=0)
        x = preprocess_input(x)
        features = model.predict(x)
        return features.flatten()
    
    # 特徴量の抽出
    features1 = preprocess(img1)
    features2 = preprocess(img2)
    
    # コサイン類似度の計算
    similarity = cosine_similarity_func(features1, features2)
    return similarity

def ssim_similarity(img1, img2):
    # 画像サイズの調整
    min_shape = (min(img1.shape[0], img2.shape[0]), min(img1.shape[1], img2.shape[1]))
    img1_cropped = img1[:min_shape[0], :min_shape[1]]
    img2_cropped = img2[:min_shape[0], :min_shape[1]]
    # SSIMの計算
    score = metrics.structural_similarity(img1_cropped, img2_cropped)
    return score

def hog_similarity(img1, img2):
    # リサイズ
    img1_resized = Image.fromarray(img1).resize((128, 128))
    img2_resized = Image.fromarray(img2).resize((128, 128))
    img1_resized = np.array(img1_resized)
    img2_resized = np.array(img2_resized)
    # HOG特徴量の計算
    features1, _ = feature.hog(img1_resized, pixels_per_cell=(8, 8), cells_per_block=(2, 2), visualize=True)
    features2, _ = feature.hog(img2_resized, pixels_per_cell=(8, 8), cells_per_block=(2, 2), visualize=True)
    # コサイン類似度の計算
    similarity = cosine_similarity_func(features1, features2)
    return similarity

def edge_structure_similarity(img1, img2):
    # Sobelフィルタによるエッジ検出
    sobel1 = ndimage.sobel(img1)
    sobel2 = ndimage.sobel(img2)
    # フラット化
    sobel1_flat = sobel1.flatten()
    sobel2_flat = sobel2.flatten()
    # コサイン類似度の計算
    similarity = cosine_similarity_func(sobel1_flat, sobel2_flat)
    return similarity

def template_matching_similarity(img1, img2):
    # テンプレートマッチングの実行
    correlation = correlate2d(img1, img2, boundary='symm', mode='same')
    max_corr = np.max(correlation)
    normalized_corr = max_corr / (np.linalg.norm(img1) * np.linalg.norm(img2))
    return normalized_corr

def fourier_similarity(img1, img2):
    # リサイズ
    img1_resized = Image.fromarray(img1).resize((256, 256))
    img2_resized = Image.fromarray(img2).resize((256, 256))
    img1_resized = np.array(img1_resized)
    img2_resized = np.array(img2_resized)
    # フーリエ変換の計算
    f1 = np.fft.fft2(img1_resized)
    f2 = np.fft.fft2(img2_resized)
    # 周波数スペクトルの取得
    magnitude_spectrum1 = np.abs(np.fft.fftshift(f1))
    magnitude_spectrum2 = np.abs(np.fft.fftshift(f2))
    # フラット化
    spectrum1_flat = magnitude_spectrum1.flatten()
    spectrum2_flat = magnitude_spectrum2.flatten()
    # コサイン類似度の計算
    similarity = cosine_similarity_func(spectrum1_flat, spectrum2_flat)
    return similarity

def cross_correlation_similarity(img1, img2):
    # 画像サイズの調整
    min_shape = (min(img1.shape[0], img2.shape[0]), min(img1.shape[1], img2.shape[1]))
    img1_cropped = img1[:min_shape[0], :min_shape[1]]
    img2_cropped = img2[:min_shape[0], :min_shape[1]]
    # クロスコリレーションの計算
    correlation = correlate2d(img1_cropped, img2_cropped, boundary='symm', mode='valid')
    max_corr = np.max(correlation)
    normalized_corr = max_corr / (np.linalg.norm(img1_cropped) * np.linalg.norm(img2_cropped))
    return normalized_corr

def gabor_similarity(img1, img2):
    # Gaborフィルタの適用
    filt_real1, _ = filters.gabor(img1, frequency=0.6)
    filt_real2, _ = filters.gabor(img2, frequency=0.6)
    # フラット化
    filt_real1_flat = filt_real1.flatten()
    filt_real2_flat = filt_real2.flatten()
    # コサイン類似度の計算
    similarity = cosine_similarity_func(filt_real1_flat, filt_real2_flat)
    return similarity

def wavelet_similarity(img1, img2):
    # リサイズ
    img1_resized = Image.fromarray(img1).resize((256, 256))
    img2_resized = Image.fromarray(img2).resize((256, 256))
    img1_resized = np.array(img1_resized)
    img2_resized = np.array(img2_resized)
    # Wavelet変換の計算
    coeffs1 = pywt.wavedec2(img1_resized, 'haar', level=2)
    coeffs2 = pywt.wavedec2(img2_resized, 'haar', level=2)
    # 特徴量のベクトル化
    # 修正: coeffs1内の各要素が配列であることを確認し、flattenを適用
    features1 = np.hstack([np.array(c).flatten() if isinstance(c, (np.ndarray, tuple, list)) else c.flatten() for c in coeffs1])  
    features2 = np.hstack([np.array(c).flatten() if isinstance(c, (np.ndarray, tuple, list)) else c.flatten() for c in coeffs2]) 
    # コサイン類似度の計算
    similarity = cosine_similarity_func(features1, features2)
    return similarity

def histogram_similarity(img1, img2):
    # ヒストグラムの計算
    hist1, _ = np.histogram(img1.flatten(), bins=256, range=(0, 256))
    hist2, _ = np.histogram(img2.flatten(), bins=256, range=(0, 256))
    # ヒストグラムの正規化
    hist1 = hist1.astype(float) / hist1.sum()
    hist2 = hist2.astype(float) / hist2.sum()
    # コサイン類似度の計算
    similarity = cosine_similarity_func(hist1, hist2)
    return similarity

def density_similarity(img1, img2):
    # バイナリ化
    threshold = 128
    binary1 = img1 > threshold
    binary2 = img2 > threshold
    # 密度の計算
    density1 = binary1.mean()
    density2 = binary2.mean()
    # 類似度の計算
    similarity = 1 - abs(density1 - density2)
    return similarity

def mse_similarity(img1, img2):
    # リサイズ
    img1_resized = Image.fromarray(img1).resize((256, 256))
    img2_resized = Image.fromarray(img2).resize((256, 256))
    img1_resized = np.array(img1_resized)
    img2_resized = np.array(img2_resized)
    # MSEの計算
    mse = np.mean((img1_resized - img2_resized) ** 2)
    similarity = 1 / (1 + mse)
    return similarity

def pixel_cosine_similarity(img1, img2):
    # リサイズ
    img1_resized = Image.fromarray(img1).resize((256, 256))
    img2_resized = Image.fromarray(img2).resize((256, 256))
    img1_resized = np.array(img1_resized)
    img2_resized = np.array(img2_resized)
    # フラット化
    vec1 = img1_resized.flatten()
    vec2 = img2_resized.flatten()
    # コサイン類似度の計算
    similarity = cosine_similarity_func(vec1, vec2)
    return similarity

def lbp_similarity(img1, img2):
    # LBP特徴量の計算
    radius = 1
    n_points = 8 * radius
    lbp1 = feature.local_binary_pattern(img1, n_points, radius, method='uniform')
    lbp2 = feature.local_binary_pattern(img2, n_points, radius, method='uniform')
    # ヒストグラムの計算
    hist1, _ = np.histogram(lbp1.ravel(), bins=np.arange(0, n_points + 3), range=(0, n_points + 2))
    hist2, _ = np.histogram(lbp2.ravel(), bins=np.arange(0, n_points + 3), range=(0, n_points + 2))
    # ヒストグラムの正規化
    hist1 = hist1.astype(float) / hist1.sum()
    hist2 = hist2.astype(float) / hist2.sum()
    # コサイン類似度の計算
    similarity = cosine_similarity_func(hist1, hist2)
    return similarity

def zernike_similarity(img1, img2, radius=64, degree=8):
    # リサイズ
    img1_resized = Image.fromarray(img1).resize((128, 128))
    img2_resized = Image.fromarray(img2).resize((128, 128))
    img1_resized = np.array(img1_resized)
    img2_resized = np.array(img2_resized)
    # バイナリ化
    threshold = 128
    binary1 = (img1_resized > threshold).astype(np.uint8)
    binary2 = (img2_resized > threshold).astype(np.uint8)
    # Zernikeモーメントの計算
    moments1 = mahotas.features.zernike_moments(binary1, radius, degree)
    moments2 = mahotas.features.zernike_moments(binary2, radius, degree)
    # コサイン類似度の計算
    similarity = cosine_similarity_func(moments1, moments2)
    return similarity

def hough_line_similarity(img1, img2):
    # エッジ検出
    edges1 = feature.canny(img1)
    edges2 = feature.canny(img2)
    # ハフ変換による直線検出
    lines1 = transform.probabilistic_hough_line(edges1)
    lines2 = transform.probabilistic_hough_line(edges2)
    # 直線の数を比較
    num_lines1 = len(lines1)
    num_lines2 = len(lines2)
    # 類似度の計算
    if max(num_lines1, num_lines2) == 0:
        similarity = 1.0
    else:
        similarity = 1 - abs(num_lines1 - num_lines2) / max(num_lines1, num_lines2)
    return similarity

def object_size_similarity(img1, img2):
    # バイナリ化
    threshold = 128
    binary1 = (img1 > threshold).astype(np.uint8)
    binary2 = (img2 > threshold).astype(np.uint8)
    # ラベリング
    labeled1, num_features1 = ndimage.label(binary1)
    labeled2, num_features2 = ndimage.label(binary2)
    # オブジェクトのサイズリスト
    sizes1 = ndimage.sum(binary1, labeled1, range(1, num_features1 + 1))
    sizes2 = ndimage.sum(binary2, labeled2, range(1, num_features2 + 1))
    # サイズヒストグラムの計算
    hist1, _ = np.histogram(sizes1, bins=10, range=(0, sizes1.max()))
    hist2, _ = np.histogram(sizes2, bins=10, range=(0, sizes2.max()))
    # ヒストグラムの正規化
    hist1 = hist1.astype(float) / hist1.sum()
    hist2 = hist2.astype(float) / hist2.sum()
    # コサイン類似度の計算
    similarity = cosine_similarity_func(hist1, hist2)
    return similarity

def pca_similarity(img1, img2, n_components=50):
    # リサイズ
    img1_resized = Image.fromarray(img1).resize((64, 64))
    img2_resized = Image.fromarray(img2).resize((64, 64))
    img1_flat = np.array(img1_resized).flatten()
    img2_flat = np.array(img2_resized).flatten()
    # データの結合
    data = np.vstack([img1_flat, img2_flat])
    # PCAの適用
    pca = PCA(n_components=n_components)
    pca_features = pca.fit_transform(data)
    # コサイン類似度の計算
    similarity = cosine_similarity_func(pca_features[0], pca_features[1])
    return similarity

def ssm_similarity(img1, img2):
    # リサイズ
    img1_resized = Image.fromarray(img1).resize((64, 64))
    img2_resized = Image.fromarray(img2).resize((64, 64))
    img1_flat = np.array(img1_resized).flatten()
    img2_flat = np.array(img2_resized).flatten()
    # 自己相似性マトリックスの計算
    ssm1 = cosine_similarity([img1_flat])
    ssm2 = cosine_similarity([img2_flat])
    # フラット化
    ssm1_flat = ssm1.flatten()
    ssm2_flat = ssm2.flatten()
    # コサイン類似度の計算
    similarity = cosine_similarity_func(ssm1_flat, ssm2_flat)
    return similarity

def angle_distribution_similarity(img1, img2):
    # エッジ検出
    edges1 = feature.canny(img1)
    edges2 = feature.canny(img2)
    # 勾配の計算
    gy1, gx1 = np.gradient(img1.astype(float))
    gy2, gx2 = np.gradient(img2.astype(float))
    # エッジ上のピクセルの角度計算
    angles1 = np.arctan2(gy1[edges1], gx1[edges1])
    angles2 = np.arctan2(gy2[edges2], gx2[edges2])
    # ヒストグラムの計算
    hist1, _ = np.histogram(angles1, bins=36, range=(-np.pi, np.pi))
    hist2, _ = np.histogram(angles2, bins=36, range=(-np.pi, np.pi))
    # ヒストグラムの正規化
    hist1 = hist1.astype(float) / hist1.sum()
    hist2 = hist2.astype(float) / hist2.sum()
    # コサイン類似度の計算
    similarity = cosine_similarity_func(hist1, hist2)
    return similarity

def size_position_similarity(img1, img2):
    # バイナリ化
    threshold = 128
    binary1 = (img1 > threshold).astype(np.uint8)
    binary2 = (img2 > threshold).astype(np.uint8)
    # ラベリング
    labeled1, num_features1 = ndimage.label(binary1)
    labeled2, num_features2 = ndimage.label(binary2)
    # サイズと位置の取得
    sizes1 = ndimage.sum(binary1, labeled1, range(1, num_features1 + 1))
    sizes2 = ndimage.sum(binary2, labeled2, range(1, num_features2 + 1))
    positions1 = ndimage.center_of_mass(binary1, labeled1, range(1, num_features1 + 1))
    positions2 = ndimage.center_of_mass(binary2, labeled2, range(1, num_features2 + 1))
    # 平均サイズと位置
    sizes1_mean = np.mean(sizes1)
    sizes2_mean = np.mean(sizes2)
    positions1_mean = np.mean(positions1, axis=0)
    positions2_mean = np.mean(positions2, axis=0)
    # サイズの類似度
    size_similarity = 1 - abs(sizes1_mean - sizes2_mean) / max(sizes1_mean, sizes2_mean)
    # 位置の類似度
    max_dim = max(img1.shape)
    position_similarity = 1 - np.linalg.norm(np.array(positions1_mean) - np.array(positions2_mean)) / max_dim
    # 総合的な類似度
    similarity = (size_similarity + position_similarity) / 2
    return similarity

def ncc_similarity(img1, img2):
    # 正規化
    img1_norm = (img1 - img1.mean()) / (img1.std() + 1e-8)
    img2_norm = (img2 - img2.mean()) / (img2.std() + 1e-8)
    # 正規化相互相関の計算
    result = feature.match_template(img2_norm, img1_norm)
    max_corr = np.max(result)
    return max_corr

def main(image_path1, image_path2):
    # 画像の読み込み
    image1 = Image.open(image_path1).convert('L')
    image2 = Image.open(image_path2).convert('L')
    # 画像サイズの調整
    image2 = image2.resize(image1.size)
    img1 = np.array(image1)
    img2 = np.array(image2)
    
    # 各手法による類似度の計算と実行時間の測定
    similarities = {}
    times = {}
    
    methods = {
        '輪郭抽出と比較': extract_contours_similarity,
        # 'ディープラーニング': deep_learning_similarity,  
        'SSIM': ssim_similarity,
        'HOG特徴量': hog_similarity,
        # 'エッジ構造': edge_structure_similarity,
        # 'テンプレートマッチング': template_matching_similarity,
        'フーリエ変換': fourier_similarity,
        # 'クロスコリレーション': cross_correlation_similarity,
        # 'Gaborフィルタ': gabor_similarity,
        'Wavelet変換': wavelet_similarity,
        'ヒストグラムの類似性': histogram_similarity,
        '文字領域の密度比較': density_similarity,
        'MSE': mse_similarity,
        # 'ピクセル値のコサイン類似度': pixel_cosine_similarity,
        'LBP特徴量': lbp_similarity,
        'Zernikeモーメント特徴量': zernike_similarity,
        'ハフ変換による直線パターン': hough_line_similarity,
        'オブジェクトの大きさ比較': object_size_similarity,
        # 'PCAによる類似性': pca_similarity,  
        'Self-Similarity Matrix': ssm_similarity,
        '角度分布の統計的比較': angle_distribution_similarity,
        'サイズと位置の分布': size_position_similarity,
        'NCCによる一致度': ncc_similarity,
        # 'SIFT特徴量マッチング': sift_similarity  
    }
    
    for method_name, method_func in methods.items():
        start_time = time.time()
        similarity = method_func(img1, img2)
        end_time = time.time()
        similarities[method_name] = similarity
        times[method_name] = end_time - start_time
        print('method: ', method_name)
        print('similarity: ', similarity)
        print('time: ', end_time - start_time)
        print()
    
    # 類似度と実行時間の表示
    print("各手法による類似度スコアと実行時間:")
    for method in similarities:
        print(f"{method}: {similarities[method]:.3f}({times[method]:.4f}s)")
    
    # 総合的な類似度（平均値）
    average_similarity = np.mean(list(similarities.values()))
    print(f"\n総合的な類似度スコア: {average_similarity:.4f}")
    
    # 総実行時間
    total_time = sum(times.values())
    print(f"総実行時間: {total_time:.4f}秒")


if __name__ == '__main__':
    # 画像パスの指定
    # 画像パスの指定
    image_path1 = '名刺1.png'
    image_path2 = '名刺2.png'
    main(image_path1, image_path2)