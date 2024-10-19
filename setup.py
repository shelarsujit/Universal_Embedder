from setuptools import setup, find_packages

setup(
    name='universal-data-embedder',
    version='1.0.0',
    author='Sujit Shelar',
    author_email='sujitshelar100@gmail.com',
    description='A universal data embedder for various file types and web links.',
    packages=find_packages(),
    install_requires=[
        'PyMuPDF',
        'pytube',
        'beautifulsoup4',
        'sentence-transformers',
        'pinecone-client',
        'python-pptx',
        'python-docx',
        'PyYAML',
        'requests',
    ],
    entry_points={
        'console_scripts': [
            'universal-embedder=main:main',
        ],
    },
)
