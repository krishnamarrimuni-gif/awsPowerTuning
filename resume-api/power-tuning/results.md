# Lambda Power Tuning Results

## Function Tested
`person-details-read` — DynamoDB GetItem operation

## Configuration
- Memory sizes tested: 128MB, 256MB, 512MB, 1024MB, 2048MB
- Invocations per size: 10
- Strategy: Cost
- Parallel invocation: true

## Results

| Memory | Avg Duration | Cost per 1M requests | Verdict |
|--------|-------------|---------------------|---------|
| 128 MB | ~30ms | Lowest | Fast on warm start |
| 256 MB | ~380ms | Medium | Worst time |
| 512 MB | ~5ms | Lowest | Best Cost + Best Time |
| 1024 MB | ~101ms | $0.0000171 | Worst cost |
| 2048 MB | ~95ms | Highest | Overkill |

## Winner: 512MB

512MB won both Best Cost and Best Time for this Lambda.

## Key Insight
Cold start vs warm start matters:
- Cold start: 512MB performs better due to faster initialization
- Warm start: 128MB is cheapest and fastest
- For low-traffic API: 512MB is the safe choice

## Decision
Updated Lambda memory to **512MB** based on power tuning results.
