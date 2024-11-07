import asyncio

from google.maps import solar_v1
from google.type import latlng_pb2


async def main():
    client = solar_v1.SolarAsyncClient.from_service_account_file("credentials.json")

    location = latlng_pb2.LatLng(latitude=-22.8447, longitude=-43.2327)

    request = solar_v1.FindClosestBuildingInsightsRequest(
        location=location,
        required_quality=solar_v1.ImageryQuality.HIGH,
        exact_quality_required=False,
    )
    response = await client.find_closest_building_insights(request=request)

    with open("output.json", "w") as f:
        f.write(str(response))


if __name__ == "__main__":
    asyncio.run(main())
