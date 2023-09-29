""" Parallel Matrix Multiplication:

Problem: Multiply two large matrices efficiently by parallelizing the computation across multiple processors or cores.
 """
import numpy as np
from multiprocessing import Pool

def multiply_row(row):
    global matrix_a, matrix_b
    return np.dot(matrix_a[row, :], matrix_b)

def parallel_matrix_multiplication(matrix_a, matrix_b, num_processes):
    global result_matrix
    result_matrix = np.zeros((matrix_a.shape[0], matrix_b.shape[1]))
    pool = Pool(processes=num_processes)
    results = pool.map(multiply_row, range(matrix_a.shape[0]))
    pool.close()
    pool.join()
    for row, result in enumerate(results):
        result_matrix[row, :] = result

if __name__ == '__main__':
    matrix_a = np.random.rand(1000, 1000)
    matrix_b = np.random.rand(1000, 1000)
    num_processes = 4
    parallel_matrix_multiplication(matrix_a, matrix_b, num_processes)

""" Distributed Web Scraping:

Problem: Scrape data from multiple websites concurrently and distribute the workload across multiple machines or processes.
 """
import requests
from concurrent.futures import ThreadPoolExecutor

def scrape_website(url):
    response = requests.get(url)
    if response.status_code == 200:
        return response.text
    return None

def distributed_web_scraping(urls):
    with ThreadPoolExecutor(max_workers=len(urls)) as executor:
        results = list(executor.map(scrape_website, urls))
    return results

if __name__ == '__main__':
    websites = ['https://example.com', 'https://example.org', 'https://example.net']
    scraped_data = distributed_web_scraping(websites)
    for data in scraped_data:
        if data:
            print(len(data))

""" Parallelized Image Processing:

Problem: Apply image processing filters (e.g., blur, edge detection) to a batch of images concurrently using parallel processing.
 """
from multiprocessing import Pool
from PIL import Image, ImageFilter
import os

def process_image(image_path):
    img = Image.open(image_path)
    img = img.filter(ImageFilter.BLUR)  # Apply a filter (e.g., blur)
    img.save(f"output/{os.path.basename(image_path)}")

def parallel_image_processing(image_paths, num_processes):
    os.makedirs("output", exist_ok=True)
    pool = Pool(processes=num_processes)
    pool.map(process_image, image_paths)
    pool.close()
    pool.join()

if __name__ == '__main__':
    image_paths = ['image1.jpg', 'image2.jpg', 'image3.jpg']
    num_processes = 3
    parallel_image_processing(image_paths, num_processes)