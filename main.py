import argparse
from pathlib import Path
from methods.CosineSimilarity import CosineSimilarity
from methods.JaccardSimilarity import JaccardSimilarity
from methods.LevenshteinSimilarity import LevenshteinSimilarity
from methods.MinHashSimilarity import MinHashSimilarity
from methods.SimHashSimilarity import SimHashSimilarity
from methods.CustomSimilarity import CustomSimilarity
from memory_profiler import memory_usage

FILE = Path(__file__).resolve()
ROOT = FILE.parents[0]  #root directory
ARTICLE = ROOT / "article"
OUTPUT = ROOT / "tests"

# 将浮点数保存到txt文件中
def save_float_to_txt(filename, float_number):
    try:
        with open(filename, 'w') as file:
            file.write(str(float_number))
        print(f"成功将 {float_number} 保存到 {filename} 中")
    except Exception as e:
        print(f"保存失败：{e}")


def parse_opt():
    parser = argparse.ArgumentParser()
    parser.add_argument('--orig-path', type=Path, default= ARTICLE / 'orig.txt', help='original article path')
    parser.add_argument('--orig-add-path', type=Path, default= ARTICLE / 'orig_add.txt', help='plagiarized article path')
    parser.add_argument('--output', type=Path, default=OUTPUT / 'ans.txt', help='save results to tests/ans.txt')
    parser.add_argument('--alpha', type=float, default=0.1, help='Hyperparameters')
    parser.add_argument('--check-method', type=str, default='cosine', help='cosine,jaccard,levenshtein,minhash,simhash')
    opt = parser.parse_args()

    return opt


def run(args):
    with open(args.orig_path, 'r') as x, open(args.orig_add_path, 'r') as y:
        content_x = x.read()
        content_y = y.read()
        if args.check_method == 'cosine':
            checker = CosineSimilarity(content_x, content_y)
            checker = checker.main()
            print('相似度: %.2f%%' % (checker * 100))
        elif args.check_method == 'jaccard':
            checker = JaccardSimilarity(content_x,content_y)
            checker = checker.main()
            print('相似度: %.2f%%' % (checker * 100))
        elif args.check_method == 'levenshtein':
            checker = LevenshteinSimilarity(content_x, content_y)
            checker=checker.main()
            print('相似度: %.2f%%' % (checker * 100))
        elif args.check_method == 'minhash':
            checker =  MinHashSimilarity(content_x, content_y)
            checker=checker.main()
            print('相似度: %.2f%%' % (checker * 100))
        elif args.check_method == 'simhash':
            checker = SimHashSimilarity(content_x, content_y)
            checker=checker.main()
            print('相似度: %.2f%%' % (checker * 100))
        elif args.check_method == 'custom':
            checker = CustomSimilarity(content_x, content_y, args.alpha)
            checker = checker.main()
            print('相似度: %.2f%%' % (checker * 100))
        # 构建文件路径
        file_path = args.output

        # 确保目录存在，如果不存在，则自动创建
        file_path.parent.mkdir(parents=True, exist_ok=True)

        save_float_to_txt(file_path, checker * 100)

def wrapped_run():
    run(opt)

if __name__ == '__main__':
    opt = parse_opt()
    mem_usage = memory_usage(wrapped_run)
    print('Memory usage (in chunks of .1 seconds): %s' % mem_usage)
    print('Maximum memory usage: %s' % max(mem_usage))

