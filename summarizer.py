import ollama
import click

@click.command()
@click.argument('input', type=str)
@click.option('--file', '-f', is_flag=True, help='Indicates that the input is a file.')
def summarize(input, file):
    """Summarizes text from a file or a direct text input."""
    if file:
        with open(input, 'r') as file:
            content = file.read()
    else:
        content = input

    my_prompt = f'This is a personal note, what is it about? {content}'
    response = ollama.generate(model='qwen2:0.5b', prompt=my_prompt)
    actual_response = response['response']

    print(f'\nSummary:\n{actual_response}')

if __name__ == '__main__':
    summarize()
