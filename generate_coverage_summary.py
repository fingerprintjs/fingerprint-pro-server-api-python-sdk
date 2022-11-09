import json

with open('coverage.json', 'r') as f:
    json_report = json.load(f)

json_summary = {
    'total': {
        'statements': {
            'pct': json_report['totals']['percent_covered']
        }
    }
}

with open('coverage-summary.json', 'w') as json_file:
    json.dump(json_summary, json_file)
